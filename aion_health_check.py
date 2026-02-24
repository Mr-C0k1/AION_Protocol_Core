import os
import json

def check_aion_integrity():
    # Daftar file wajib untuk Protokol AION
    required_files = {
        "metadata.json": "Pusat Data Identitas Agen",
        "package.json": "Konfigurasi Dependensi Sistem",
        "NETWORK_MAP.md": "Dokumentasi Arsitektur Jaringan",
        "core/aion_integrator.py": "Kernel Logika AION"
    }
    
    print("=== AION SYSTEM HEALTH CHECK ===")
    print(f"Status: Memverifikasi Infrastruktur Web4...\n")
    
    missing_files = 0
    
    for file_path, description in required_files.items():
        if os.path.exists(file_path):
            # Validasi tambahan untuk file JSON
            if file_path.endswith('.json'):
                try:
                    with open(file_path, 'r') as f:
                        json.load(f)
                    status = "[ OK ] Valid JSON"
                except Exception:
                    status = "[ ERR ] Corrupted JSON"
                    missing_files += 1
            else:
                status = "[ OK ] Exists"
            
            print(f"✔️ {file
