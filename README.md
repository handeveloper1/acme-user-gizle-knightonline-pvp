🧱 acme-user-gizle-knightonline-pvp
🚀 PyMem Toolkit
<p align="center"> <img src="https://img.shields.io/badge/Python-3.9%20--%203.13-blue?logo=python" alt="Python"> <img src="https://img.shields.io/badge/Platform-Windows-green?logo=windows" alt="Platform"> <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"> </p>
📖 Proje Hakkında

Bu proje Python kullanılarak geliştirilmiştir ve belirli işlemleri otomatikleştirmeye yönelik bir arayüz içerir.
Orijinal sistemde “SimpleGui” gibi ücretli bir kütüphane kullanılmıştı; bu proje, o yapıyı kaldırıp tkinter tabanlı bir arayüzle yeniden düzenlenmiştir.

Kütüphaneler yüklendikten sonra Python dosyasını çalıştırarak sisteminizi test edebilirsiniz.
İsterseniz pyinstaller ile .exe oluşturup farklı cihazlarda kullanabilirsiniz.

📦 Gerekli Kütüphaneler

Projenin sorunsuz çalışması için aşağıdaki kütüphaneleri kurmanız gerekir:

pip install pymem psutil tkinter


💡 Not:
Tkinter genellikle Python ile birlikte gelir.
Eksikse şu komutu kullanabilirsiniz:

sudo apt-get install python3-tk   # Linux için

🐍 Minimum Python Sürümü

Python 3.9 – 3.13 sürümleri arasında sorunsuz çalışır.

⚙️ Nasıl Çalıştırılır

1️⃣ Yukarıdaki kütüphaneleri yükleyin.
2️⃣ Dosyayı çalıştırın:

python main.py


3️⃣ Dilerseniz pyinstaller ile .exe oluşturabilirsiniz:

pyinstaller --onefile --noconsole main.py


4️⃣ Oluşturulan .exe dosyasını başka bilgisayarlarda da kolayca çalıştırabilirsiniz.

🧩 Kullanım Talimatı

Kütüphaneleri kurduktan sonra python dosyasını çalıştırın.
İsterseniz .exe hâline getirip başka bilgisayarlarda da çalıştırabilirsiniz.
Gerekli dosyaları seçip “User Gizle” adımını tamamlayın — işlem tamamdır ✅

🧠 Kullanılan Kütüphaneler
import pymem
import pymem.process
import psutil
import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading

💡 Ek Bilgi

Proje, Python GUI (tkinter) ve bellek işlemleriyle etkileşen modüller üzerinde temel örnek niteliği taşır.
İlerleyen sürümlerde ek işlevler veya hata ayıklama özellikleri eklenebilir.
