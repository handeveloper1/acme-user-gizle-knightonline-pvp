🧱 acme-user-gizle-knightonline-pvp
🚀 PyMem Toolkit
<p align="center"> <img src="https://img.shields.io/badge/Python-3.9%20--%203.13-blue?logo=python" alt="Python"> <img src="https://img.shields.io/badge/Platform-Windows-green?logo=windows" alt="Platform"> <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"> </p>
📦 Gerekli Kütüphaneler

Bu projeyi kullanabilmek için aşağıdaki kütüphaneleri kurmanız gerekir:

pip install pymem psutil tkinter


💡 Not:
Tkinter genellikle Python ile birlikte gelir, ancak eksikse aşağıdaki komutu deneyebilirsiniz:

sudo apt-get install python3-tk   # Linux için



🐍 Minimum Python Sürümü

Python 3.9 – 3.13 arasında sorunsuz çalışır.



⚙️ Nasıl Çalıştırılır

Yukarıdaki kütüphaneleri yükleyin.

Dosyayı şu şekilde çalıştırın:

python main.py



Dilerseniz pyinstaller kullanarak .exe hâline getirebilirsiniz:

pyinstaller --onefile --noconsole main.py




Böylece dosyayı farklı bilgisayarlarda da kolayca çalıştırabilirsiniz.



🧩 Kullanım Talimatı

Kütüphaneleri kurduktan sonra pythonu çalıştırın.
İsterseniz pyinstaller ile .exe yapıp diğer bilgisayarlarınıza atabilirsiniz.
Acme serverlarının .exe dosyalarını seçin, User Gizle’ye tıklayın — işlem tamam ✅



🧠 Kullanılan Kütüphaneler
import pymem
import pymem.process
import psutil
import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
