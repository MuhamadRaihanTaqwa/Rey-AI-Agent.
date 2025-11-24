import sys
import time
import random
import string
import psutil
import sys
import time
import random
import string
import psutil
import os  
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

# --- FUNGSI ESTETIKA (VISUAL) ---
def ketik_efek(text, delay=0.03, warna=Fore.GREEN):
    """Membuat efek teks muncul satu per satu seperti diketik"""
    sys.stdout.write(warna)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def loading_bar(durasi=2, pesan="PROCESS"):
    """Menampilkan animasi loading bar"""
    print(Fore.YELLOW + f"[{pesan}] Memulai proses...")
    toolbar_width = 30
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(durasi / toolbar_width)
        sys.stdout.write(Fore.CYAN + "█")
        sys.stdout.flush()
    sys.stdout.write(Style.RESET_ALL + "]\n")

def tampilkan_header():
    # ASCII Art bertuliskan "REY AGENT" (Versi Fixed Y)
    ascii_art = r"""
  _____  _______   __
 |  __ \|  ___\ \ / /
 | |__) | |__  \ V / 
 |  _  /|  __|  | |  
 | | \ \| |____ | |  
 |_|  \_\______||_|  
                      
      _    ____ _____ _   _ _____ 
     / \  / ___| ____| \ | |_   _|
    / _ \| |  _|  _| |  \| | | |  
   / ___ \ |_| | |___| |\  | | |  
  /_/   \_\____|_____|_| \_| |_|  
    """
    
    print(Fore.CYAN + Style.BRIGHT + ascii_art)
    print(Fore.WHITE + "==================================================")
    print(Fore.WHITE + "   REY INTELLIGENT SYSTEM V.3.0 - ONLINE")
    print(Fore.WHITE + "==================================================\n")

# --- CUSTOM TOOLS (Fungsi Unik) ---
def tool_generate_password(panjang=12):
    """Tool 1: Membuat password acak yang kuat"""
    loading_bar(1.5, "ENCRYPTING")
    karakter = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(karakter) for i in range(panjang))
    return f"Password Aman Terbuat: {password}"

def tool_scan_network():
    """Tool 2: Simulasi scan ping jaringan"""
    loading_bar(2, "NETWORK SCAN")
    ping = random.randint(15, 120)
    status = "STABIL" if ping < 50 else "LAMBAT"
    if ping < 50: warna_ping = Fore.GREEN 
    else: warna_ping = Fore.RED
    
    return (f"Status Jaringan:\n"
            f"- Ping Latency : {warna_ping}{ping} ms{Fore.WHITE}\n"
            f"- Status Koneksi: {status}")

def tool_system_check():
    """Tool 3: Cek Hardware (Fitur lama yang diperbagus)"""
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    
    warna_cpu = Fore.RED if cpu > 70 else Fore.GREEN
    warna_ram = Fore.RED if ram > 80 else Fore.GREEN
    
    return (f"Diagnosa Sistem:\n"
            f"- Beban CPU : {warna_cpu}{cpu}%\n"
            f"- Beban RAM : {warna_ram}{ram}%")
def tool_catat_rahasia(pesan):
    """Tool 4: Mencatat pesan user ke file external"""
    loading_bar(1, "SAVING DATA")
    
    # Membersihkan kata perintah (misal menghapus kata 'catat')
    isi_catatan = pesan.replace("catat", "").replace("tulis", "").strip()
    
    # Menyimpan ke file txt
    nama_file = "rahasia_agent.txt"
    with open(nama_file, "a") as f:
        waktu = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{waktu}] {isi_catatan}\n")
    
    return (f"DATA TERENKRIPSI TERSIMPAN.\n"
            f"- Lokasi File : {nama_file}\n"
            f"- Isi Pesan   : '{isi_catatan}'")

def tool_cari_file(keyword_pencarian):
    """Tool 5: Mencari file di Drive C dengan Metode 'Flexible Keywords'"""
    
    folder_awal = "C:\\"
    
    print(Fore.YELLOW + f"[INFO] Target Pencarian: Seluruh Drive C: (User Custom Folders)")
    loading_bar(5, "ROOT SEARCHING") 
    
    hasil_pencarian = []
    
    # 1. Daftar Kata Sampah (Stopwords)
    kata_diabaikan = [
        "tolong", "carikan", "cari", "lokasi", "spesifik", "file", 
        "di", "laptop", "saya", "kamu", "dong", "folder", "nama", "yang", "berjudul"
    ]
    
    # 2. Pecah kalimat user menjadi list kata-kata bersih
    raw_words = keyword_pencarian.split()
    keywords_bersih = []
    
    for kata in raw_words:
        # Bersihkan tanda baca, lalu ubah ke huruf kecil
        kata_clean = kata.strip(".,?!").lower()
        if kata_clean and kata_clean not in kata_diabaikan:
            keywords_bersih.append(kata_clean)
            
    # Gabungkan kembali untuk display log saja
    target_display = " + ".join(keywords_bersih)
    print(Fore.YELLOW + f"[SEARCH] Mencari file yang mengandung kata: [{target_display}]...")

    # --- PROSES PENCARIAN (ROOT C:) ---
    limit_file = 5 
    folder_dilarang = [
        'Windows', 'Program Files', 'Program Files (x86)', 
        'ProgramData', '$Recycle.Bin', 'System Volume Information', 'AppData'
    ]
    
    for root, dirs, files in os.walk(folder_awal):
        
        # Skip folder sistem
        skip_folder = False
        for dilarang in folder_dilarang:
            if dilarang in root:
                skip_folder = True
                break
        if skip_folder:
            continue
            
        try:
            for file in files:
                nama_file_lower = file.lower()
                
                # --- LOGIKA BARU: MULTI-WORD MATCHING ---
                # Semua keyword harus ada di nama file, urutan tidak masalah
                semua_kata_ada = True
                for k in keywords_bersih:
                    if k not in nama_file_lower:
                        semua_kata_ada = False
                        break
                
                if semua_kata_ada:
                    full_path = os.path.join(root, file)
                    hasil_pencarian.append(full_path)
                    
                    if len(hasil_pencarian) >= limit_file:
                        break 
        
        except PermissionError:
            continue 
            
        if len(hasil_pencarian) >= limit_file:
            break

    # --- OUTPUT ---
    if hasil_pencarian:
        laporan = f"FILE DITEMUKAN ({len(hasil_pencarian)} hasil teratas):\n"
        for path in hasil_pencarian:
            laporan += f"- {path}\n"
        return laporan
    else:
        return f"File dengan kombinasi kata '{target_display}' tidak ditemukan."
# --- LOGIKA OTAK AI ---
def otak_ai(input_user):
    text = input_user.lower()
    
    # --- LOGIKA PRIORITAS TINGGI (Tools Spesifik) ---
    
    # 1. Cek Kata Kunci Password
    if "password" in text or "sandi" in text:
        ketik_efek("[AI] Mengaktifkan modul Generator Kriptografi...", 0.02, Fore.YELLOW)
        return tool_generate_password()
    
    # 2. Cek Kata Kunci Pencarian File (HARUS DI ATAS 'LAPTOP')
    elif "cari" in text or "lokasi" in text or "dimana" in text:
        ketik_efek("[AI] Memindai direktori penyimpanan...", 0.02, Fore.YELLOW)
        return tool_cari_file(text)

    # 3. Cek Kata Kunci Catat Note
    elif "catat" in text or "tulis" in text or "note" in text:
        ketik_efek("[AI] Membuka akses memori eksternal...", 0.02, Fore.YELLOW)
        return tool_catat_rahasia(text)
    
    # 4. Cek Kata Kunci Internet
    elif "internet" in text or "jaringan" in text or "wifi" in text or "ping" in text:
        ketik_efek("[AI] Melakukan ping ke server global...", 0.02, Fore.YELLOW)
        return tool_scan_network()
    
    # 5. Cek Hardware (Keyword 'laptop' ditaruh di sini agar tidak konflik)
    elif "cpu" in text or "ram" in text or "sistem" in text or "laptop" in text:
        ketik_efek("[AI] Membaca sensor hardware...", 0.02, Fore.YELLOW)
        return tool_system_check()
    
    # --- LOGIKA LAINNYA ---
    elif "keluar" in text:
        return "EXIT"
    
    elif "halo" in text:
        return "Sistem Online. Siap menjalankan tugas."
        
    else:
        return "Perintah tidak dikenali. Coba: 'Cari file [nama]', 'Buat Password', atau 'Cek sistem'."

# --- MAIN LOOP ---
def main():
    tampilkan_header()
    
    while True:
        try:
            user_input = input(Fore.MAGENTA + Style.BRIGHT + "USER COMMAND >> " + Fore.WHITE)
        except KeyboardInterrupt:
            print("\nForce Close.")
            break

        if not user_input: continue
        
        response = otak_ai(user_input)
        
        if response == "EXIT":
            ketik_efek("SHUTTING DOWN SYSTEM...", 0.05, Fore.RED)
            break
            
        print(Fore.CYAN + "--------------------------------------------------")
        print(Fore.CYAN + "AI RESPONSE:")
        print(Fore.WHITE + response)
        print(Fore.CYAN + "--------------------------------------------------\n")

if __name__ == "__main__":
    main()