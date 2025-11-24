# 🕵️ REY AGENT - Intelligent Terminal System (V.3.0)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey) ![Status](https://img.shields.io/badge/Status-Active-green)

**Rey Agent** adalah asisten virtual berbasis *Command Line Interface* (CLI) yang dirancang dengan estetika *hacker/sci-fi*. Agent ini berfungsi untuk meningkatkan produktivitas developer dan *power user* melalui perintah bahasa natural (*Natural Language*).

Dirancang untuk menyelesaikan masalah pencarian file yang kompleks dan monitoring sistem tanpa perlu meninggalkan terminal.

```text
  _____  _______   __
 |  __ \|  ___\ \ / /
 | |__) | |__  \ V / 
 |  _  /|  __|  | |  
 | | \ \| |____ | |  
 |_|  \_\______||_|  
                      
   REY INTELLIGENT SYSTEM V.3.0 - ONLINE
🚀 Fitur Unggulan
1. 🔍 Deep Search Engine (Pencarian File Canggih)
Berbeda dengan pencarian standar, Rey Agent mampu memindai seluruh Drive C: (termasuk folder user nested seperti Documents/Downloads) untuk menemukan file spesifik.
Smart Logic: Melewati folder sistem berat (Windows/AppData) agar pencarian cepat.
Flexible Keyword: Mencari berdasarkan kombinasi kata (misal: "skripsi bab 1") tanpa harus sesuai urutan persis.

2. 💻 System Health Monitor
Memantau kesehatan hardware secara real-time menggunakan library psutil.
Cek penggunaan RAM & CPU.
Indikator visual status sistem.

3. 🔐 Security & Utility
Password Generator: Membuat password acak yang kuat (huruf, angka, simbol) untuk keamanan akun.
Secret Note: Mencatat log/catatan cepat ke dalam file eksternal (.txt).
Network Check: Simulasi pengecekan latensi jaringan (Ping).

4. 🎨 Futuristic Interface
Typing Effect: Respon AI diketik huruf demi huruf.
Loading Bars: Animasi visual saat proses berat berjalan.
Color Coded: Pewarnaan teks dinamis (User: Ungu, AI: Cyan, Proses: Kuning) menggunakan colorama.

📦 Cara Instalasi & Menjalankan
Pastikan kamu sudah menginstall Python di komputer kamu.
1. Clone atau Download repository ini.
2. Install Library yang dibutuhkan via terminal/CMD:
pip install colorama psutil
3. jalankan program:
python agent_tugas.py

🤖 Contoh Perintah (Commands)
Rey Agent menggunakan pemrosesan bahasa sederhana. Kamu bisa mengetik perintah seperti berbicara dengan manusia. Berikut kata kunci (keywords) yang bisa dicoba:
Fitur,Contoh Input User
- Cari File"Tolong carikan : file skripsi saya
,Cari lokasi file foto liburan.jpg
- Cek Sistem : Gimana kondisi cpu laptop?
,Cek ram
- Keamanan : Buatkan saya password instagram
- Catatan : Catat besok ada rapat jam 9 pagi
- Jaringan : Cek koneksi internet
- Keluar : Keluar / Exit

🛠️ Struktur Project
agent_tugas.py: File utama (Main Code) yang berisi seluruh logika AI, Custom Tools, dan Interface.
rahasia_agent.txt: File output otomatis yang dibuat saat menggunakan fitur "Catat".

👨‍💻 Author
Dibuat untuk memenuhi Tugas Implementasi AI Agent. Developed by Muhamad Raihan Taqwa
