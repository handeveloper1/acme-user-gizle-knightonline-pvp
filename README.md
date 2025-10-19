🧱 acme-user-gizle-knightonline-pvp
🚀 PyMem Toolkit
<p align="center"> <img src="https://img.shields.io/badge/Python-3.9%20--%203.13-blue?logo=python" alt="Python"> <img src="https://img.shields.io/badge/Platform-Windows-green?logo=windows" alt="Platform"> <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"> </p>

## 📖 Proje Hakkında

Cheat Engine bulduğunuz user gizleme offset'inin pythonda memory write/read için derlenmiş bir demosudur.
Yarın öbürgün ofsetler adresler değişir ise cheat engineden adressleri bulup güncellediğinizde çalışacaktır.
Kötü bir amaç taşımaz. Sadece oyunucu gizleyip daha düşük sistemler minimum kaynak kullanımı hedefler.

Aynı anda birden çok client için uygulayabilirsiniz.

Kütüphaneler yüklendikten sonra Python dosyasını çalıştırarak sisteminizi test edebilirsiniz.
İsterseniz pyinstaller ile .exe oluşturup farklı cihazlarda kullanabilirsiniz.


```bash
Ben yeni python öğreniyorum bune diyorsanız kodu chat'e atın şunu diyin; ben python bilmiyorum elimde acme.client exeyi otomatik seçip bu memory write'ı uygulasın. listeden ben seçmek istemiyorum gibi bir cümle kurun o ktinkterdaki çalışan kısmını alıp daha yalın bir hale getirecektir daha rahat anlamanızı sağlayacaktır.
```


## ⚙️ Kurulum

📌 Kütüphaneleri yüklemek için terminalde şu komutu çalıştırın:

<p align="center"> <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="120"/> </p>

```bash
pip install pymem psutil tkinter pyinstaller
```


## 💡 Not:
Tkinter genellikle Python ile birlikte gelir.
Eksikse şu komutu kullanabilirsiniz:

sudo apt-get install python3-tk   # Linux için

## 🐍 Minimum Python Sürümü
```bash
Python 3.9 – 3.13 sürümleri arasında sorunsuz çalışır.
```
## ⚙️ Nasıl Çalıştırılır

1️⃣ Yukarıdaki kütüphaneleri yükleyin.
2️⃣ Dosyayı çalıştırın:
```bash
python main.py
```

3️⃣ Dilerseniz pyinstaller ile .exe oluşturabilirsiniz:
```bash
pyinstaller --onefile --noconsole main.py
```

4️⃣ Oluşturulan .exe dosyasını başka bilgisayarlarda da kolayca çalıştırabilirsiniz.

## 🧩 Kullanım Talimatı

Kütüphaneleri kurduktan sonra python dosyasını çalıştırın.
İsterseniz .exe hâline getirip başka bilgisayarlarda da çalıştırabilirsiniz.
Gerekli dosyaları seçip “User Gizle” adımını tamamlayın — işlem tamamdır ✅

## 🧠 Kullanılan Kütüphaneler
import pymem
import pymem.process
import psutil
import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading

## 💡 Ek Bilgi

Proje, Python GUI (tkinter) ve bellek işlemleriyle etkileşen modüller üzerinde temel örnek niteliği taşır.
İlerleyen sürümlerde ek işlevler veya hata ayıklama özellikleri eklenebilir.


<img width="1665" height="864" alt="image" src="https://github.com/user-attachments/assets/8ebfd98e-722c-4dfa-8212-4f623e038f50" />

<img width="1465" height="774" alt="image" src="https://github.com/user-attachments/assets/042adb36-cbac-428b-8a42-e68b442152ab" />
