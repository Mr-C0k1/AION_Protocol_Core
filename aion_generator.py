import google.generativeai as genai
import json
import os

class AIONNetwork:
    def __init__(self, api_key):
        """Inisialisasi koneksi ke Kernel AION di Cloud."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_handshake(self, node_role="General Agent"):
        """
        Membuat protokol jabat tangan (Handshake) standar untuk node baru.
        Fungsi ini bersifat umum untuk semua pengguna jaringan.
        """
        prompt = f"""
        Act as AION Kernel. Generate a standard Handshake Protocol for a new node.
        Role: {node_role}
        Include: Peer_ID, Access_Token (Encrypted), and Initial_Reputation.
        Return ONLY pure JSON.
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Membersihkan output markdown jika ada
            clean_json = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(clean_json)
        except Exception as e:
            return {"error": str(e)}

    def save_node_state(self, data, folder="aion_nodes"):
        """Menyimpan status node secara lokal di komputer pengguna."""
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        filename = f"{folder}/node_{data.get('Peer_ID', 'unknown')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return filename

# Contoh Penggunaan Umum (Bisa dijalankan siapa saja)
if __name__ == "__main__":
    # Pengguna memasukkan API Key mereka sendiri
    USER_API_KEY = "MASUKKAN_API_KEY_ANDA_DISINI"
    
    if USER_API_KEY == "MASUKKAN_API_KEY_ANDA_DISINI":
        print("Peringatan: Harap masukkan API Key AI Studio Anda.")
    else:
        aion = AIONNetwork(USER_API_KEY)
        print("Menghubungkan ke AION Network...")
        
        # Mendaftarkan node sebagai penyedia komputasi (Miner)
        new_node = aion.generate_handshake(node_role="Computing Resource Provider")
        
        if "error" not
