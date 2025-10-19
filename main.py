import pymem
import pymem.process
import psutil
import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading


ADDITIONAL_BASE2 = 0x140deaa90
OFFSET_VISIBILITY = 0x50


class UserHideBot:
    def __init__(self):
        self.attached_processes = []
        self.running = False
        self.user_hide_enabled = False
        self.root = tk.Tk()
        self.root.title("Acme User Hide Control - Memory Writer")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        self.setup_gui()
        self.refresh_process_list()

    def setup_gui(self):
        process_frame = tk.LabelFrame(self.root, text="Select Process", padx=10, pady=10)
        process_frame.pack(padx=10, pady=10, fill="both", expand=True)
        list_frame = tk.Frame(process_frame)
        list_frame.pack(fill="both", expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        self.process_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=("Consolas", 10),
            height=8,
            selectmode=tk.MULTIPLE
        )
        self.process_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.process_listbox.yview)
        tk.Label(process_frame, text="TIP: Hold Ctrl to select multiple processes",
                 font=("Segoe UI", 9, "italic"), fg="blue").pack(pady=2)
        btn_frame = tk.Frame(process_frame)
        btn_frame.pack(fill="x", pady=5)

        self.btn_refresh = tk.Button(
            btn_frame,
            text="🔄 Refresh List",
            command=self.refresh_process_list,
            font=("Segoe UI", 10)
        )
        self.btn_refresh.pack(side="left", padx=5)

        self.btn_attach = tk.Button(
            btn_frame,
            text="✓ Attach to Selected",
            command=self.attach_to_selected,
            font=("Segoe UI", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049"
        )
        self.btn_attach.pack(side="left", padx=5)
        attached_frame = tk.LabelFrame(self.root, text="Attached Processes", padx=10, pady=5)
        attached_frame.pack(padx=10, pady=5, fill="x")

        self.attached_label = tk.Label(
            attached_frame,
            text="No processes attached",
            anchor="w",
            justify="left"
        )
        self.attached_label.pack(fill="x")
        info_frame = tk.LabelFrame(self.root, text="Memory Information", padx=10, pady=5)
        info_frame.pack(padx=10, pady=5, fill="x")

        tk.Label(info_frame, text=f"Base Address: 0x{ADDITIONAL_BASE2:X}", anchor="w").pack(fill="x")
        tk.Label(info_frame, text=f"Offset: 0x{OFFSET_VISIBILITY:X}", anchor="w").pack(fill="x")
        tk.Label(info_frame, text="Value: 0 = Hidden, 1 = Visible", anchor="w").pack(fill="x")
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(fill="both")
        self.var_user_hide = tk.BooleanVar()
        self.check_user_hide = tk.Checkbutton(
            control_frame,
            text="Hide User",
            variable=self.var_user_hide,
            command=self.toggle_user_hide,
            font=("Segoe UI", 12),
            state="disabled"
        )
        self.check_user_hide.pack(pady=5)
        self.status_label = tk.Label(
            control_frame,
            text="Select a process and click 'Attach'",
            relief="sunken",
            anchor="w",
            padx=5,
            pady=5
        )
        self.status_label.pack(fill="x", pady=5)

    def refresh_process_list(self):
        self.process_listbox.delete(0, tk.END)
        self.process_dict = {}
        acme_detected = False

        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    name = proc.info['name']
                    pid = proc.info['pid']
                    if name.lower() == 'client.acme' or name.lower() == 'client.acme.exe':
                        acme_detected = True

                    if name.endswith('.exe') or name.endswith('.acme'):
                        processes.append((name, pid))
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            processes.sort(key=lambda x: x[0].lower())
            for name, pid in processes:
                display_text = f"{name:<40} (PID: {pid})"
                self.process_listbox.insert(tk.END, display_text)
                self.process_dict[display_text] = (name, pid)
            if acme_detected:
                self.update_status(f"⚠️ WARNING: client.acme detected! Found {len(processes)} processes", color="red")
            else:
                self.update_status(f"Found {len(processes)} processes")

        except Exception as e:
            self.update_status(f"hata1: {str(e)}")
    def attach_to_selected(self):
        selections = self.process_listbox.curselection()
        if not selections:
            messagebox.showwarning("No Selection", "Please select at least one process!")
            return

        success_count = 0
        for selection in selections:
            selected_text = self.process_listbox.get(selection)
            process_name, pid = self.process_dict[selected_text]

            if self.attach_to_process(process_name, pid):
                success_count += 1

        if success_count > 0:
            self.update_status(f"Program selected: {success_count} process(es) attached")
            self.check_user_hide.config(state="normal")
            self.update_attached_list()
        else:
            self.update_status("Failed to attach to any process", color="red")

    def attach_to_process(self, process_name, pid):
        try:
            for pm, name, proc_pid in self.attached_processes:
                if proc_pid == pid:
                    self.update_status(f"Already attached to {process_name} (PID: {pid})")
                    return True

            pm = pymem.Pymem()
            pm.open_process_from_id(pid)
            self.attached_processes.append((pm, process_name, pid))

            return True

        except pymem.exception.ProcessNotFound:
            messagebox.showerror("Error", f"Could not find process: {process_name} (PID: {pid})")
            return False
        except pymem.exception.CouldNotOpenProcess:
            messagebox.showerror("Error",
                                 f"Access denied to '{process_name}' (PID: {pid})! Try running as Administrator.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to attach to {process_name} (PID: {pid}): {str(e)}")
            return False

    def update_attached_list(self):
        if not self.attached_processes:
            self.attached_label.config(text="No processes attached")
        else:
            process_info = [f"{name} (PID: {pid})" for pm, name, pid in self.attached_processes]
            self.attached_label.config(text="\n".join(process_info))

    def read_base_address(self, pm):
        try:
            if pm is None:
                return None
            base = pm.read_ulonglong(ADDITIONAL_BASE2)
            return base if base != 0 else None
        except Exception as e:
            print(f"Error reading base: {e}")
            return None

    def write_visibility(self, pm, process_name, value):
        try:
            if pm is None:
                return False

            base = self.read_base_address(pm)
            if base is None:
                return False

            target_address = base + OFFSET_VISIBILITY
            pm.write_int(target_address, value)
            return True

        except Exception as e:
            print(f"Error writing to {process_name}: {e}")
            return False

    def write_visibility_all(self, value):
        success_count = 0
        for pm, process_name, pid in self.attached_processes:
            if self.write_visibility(pm, process_name, value):
                success_count += 1

        status = "Hidden" if value == 0 else "Visible"
        self.update_status(f"✓ User Hide: {status} ({success_count}/{len(self.attached_processes)} processes)")
        return success_count > 0

    def toggle_user_hide(self):
        self.user_hide_enabled = self.var_user_hide.get()

        if self.user_hide_enabled:
            self.write_visibility_all(0)  # Hide
        else:
            self.write_visibility_all(1)  # Show

    def update_status(self, message, color="black"):
        """Update status label"""
        self.status_label.config(text=message, fg=color)
        self.root.update()

    def monitor_thread(self):
        while self.running:
            try:
                if self.user_hide_enabled and len(self.attached_processes) > 0:
                    # Re-apply hide in case game resets it
                    for pm, process_name, pid in self.attached_processes:
                        base = self.read_base_address(pm)
                        if base is not None:
                            target_address = base + OFFSET_VISIBILITY
                            try:
                                current_value = pm.read_int(target_address)
                                if current_value != 0:  # If game reset it to visible
                                    self.write_visibility(pm, process_name, 0)  # Re-hide
                            except:
                                pass

                time.sleep(0.1)
            except Exception as e:
                print(f"Monitor error: {e}")
                time.sleep(1)

    def on_closing(self):
        self.running = False
        if self.user_hide_enabled and len(self.attached_processes) > 0:
            self.write_visibility_all(1)
        time.sleep(0.2)
        for pm, process_name, pid in self.attached_processes:
            try:
                pm.close_process()
            except:
                pass

        self.root.destroy()

    def run(self):
        self.running = True

        monitor = threading.Thread(target=self.monitor_thread, daemon=True)
        monitor.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()


if __name__ == "__main__":
    try:
        app = UserHideBot()
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        input("Press Enter to exit...")