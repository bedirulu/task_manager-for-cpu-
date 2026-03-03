EN



Rich,Psutil



A terminal-based, real-time CPU monitoring dashboard (Task Manager) developed entirely from scratch in Python. This tool automatically detects the cores in your system and reflects the load of each one onto the screen using dynamic progress bars and a live-updating table.



Built on the foundations of DevSecOps and System Administration, it was coded to practice reading hardware data and designing terminal user interfaces (TUI).



✨ Features

Real-Time Monitoring: Fetches current hardware data every 0.5 seconds without overloading the system.



Per-Core Tracking: Dynamically finds the number of CPU cores and creates a separate progress bar for each.



Sleek Terminal Interface: Offers a colorful, framed, and live dashboard using the rich library.



🛠️ Installation and Usage

Clone the repository to your computer:



Bash



git clone \[https://github.com/bedirulu/task\_manager.git](https://github.com/bedirulu/task\_manager.git)

cd task\_manager

Install the required libraries:



Bash



pip install -r requirements.txt

Run the tool:



Bash



python task\_manager.py





TR



Python ile tamamen sıfırdan geliştirilmiş, terminal tabanlı gerçek zamanlı bir CPU izleme paneli (Görev Yöneticisi). Bu araç, sisteminizdeki çekirdekleri otomatik olarak algılar ve her birinin yükünü dinamik çubuklar ve anlık güncellenen bir tablo ile ekrana yansıtır.



DevSecOps ve Sistem Yönetimi temelleri üzerine inşa edilmiş olup, donanım verilerinin okunması ve terminal arayüzü (TUI) tasarımı konularında pratik yapmak amacıyla kodlanmıştır.



\### ✨ Özellikler

\* \*\*Gerçek Zamanlı İzleme:\*\* Sistemi yormadan her 0.5 saniyede bir güncel donanım verisini çeker.

\* \*\*Çekirdek Bazlı Takip:\*\* İşlemcinizin çekirdek sayısını dinamik olarak bulur ve her biri için ayrı bir ilerleme çubuğu oluşturur.

\* \*\*Şık Terminal Arayüzü:\*\* `rich` kütüphanesi kullanılarak renkli, çerçeveli ve canlı bir dashboard (gösterge paneli) sunar.



\### 🛠️ Kurulum ve Çalıştırma



1\. Projeyi bilgisayarınıza indirin:

```bash

git clone \[https://github.com/bedirulu/task\_manager.git](https://github.com/bedirulu/task\_manager.git)

cd task\_manager

Gerekli kütüphaneleri kurun:



Bash



pip install -r requirements.txt

Aracı çalıştırın:



Bash



python task\_manager.py

