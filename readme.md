EN



Rich,Psutil


Development Process 


This project was developed using an active learning methodology rather than "vibe coding" (blindly generating code). The development followed a structured engineering path:

UI-First Approach: In the initial phase, a static TUI (Terminal User Interface) skeleton was built using only the rich library, without any hardware hooks. The goal was to define the User Experience (UX) and Layout before handling complex data streams.

Guided Learning with AI: Artificial Intelligence was utilized as a Senior Mentor rather than a mere code generator. Instead of requesting a full solution, the logic behind core functions (Live, Layout, Table) and library import processes were explored through active inquiry and documentation analysis.

Data Integration: Once the visual framework was finalized, the psutil library was integrated to feed actual hardware metrics (per-core CPU usage) into the interface in real-time.

Hardware Awareness: To ensure portability, hardware detection logic was implemented, allowing the dashboard to dynamically adapt to systems with varying CPU core counts.


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



Geliştirme Süreci (Behind the Scenes)

Bu proje, "vibe coding" (rastgele kodlama) yerine aktif öğrenme metodolojisi ile geliştirilmiştir:

UI First Approach: İlk aşamada psutil kullanmadan, sadece rich kütüphanesi ile statik bir TUI (Terminal User Interface) iskeleti kuruldu. Amaç, kullanıcı deneyimini ve yerleşimi (Layout) önceden belirlemekti.

Guided Learning with AI: Yapay zeka bir kod jeneratörü olarak değil, bir Senior Mentor olarak konumlandırıldı. Fonksiyonların (Live, Layout, Table) mantığı ve kütüphane import süreçleri sorgulanarak öğrenildi.

Data Integration: Görsel yapı oturduktan sonra psutil kütüphanesi entegre edilerek, sistemin gerçek donanım verileriyle (per-core CPU usage) canlı akış sağlandı.

Hardware Awareness: Kodun farklı işlemci çekirdek sayılarına dinamik olarak uyum sağlaması için donanım algılama mantığı kurgulandı.




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


