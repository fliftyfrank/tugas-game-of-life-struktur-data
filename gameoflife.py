"""
GAME OF LIFE - Conway's Game of Life
Menggunakan ADT Array sesuai dokumen!
"""

from array import Array

class GameOfLife:
    def __init__(self, baris, kolom):
        """Inisialisasi grid Game of Life ukuran baris x kolom"""
        self.baris = baris
        self.kolom = kolom
        # Grid utama: Array of Array!
        self.grid = Array(baris)
        for i in range(baris):
            # Setiap baris adalah array sepanjang kolom
            row = Array(kolom)
            row.clearing(0)  # 0 = mati, 1 = hidup
            self.grid.setitem(i, row)
    
    def set_hidup(self, baris, kolom):
        """Membuat sel menjadi hidup (1)"""
        if 0 <= baris < self.baris and 0 <= kolom < self.kolom:
            row = self.grid.getitem(baris)
            row.setitem(kolom, 1)
    
    def set_mati(self, baris, kolom):
        """Membuat sel menjadi mati (0)"""
        if 0 <= baris < self.baris and 0 <= kolom < self.kolom:
            row = self.grid.getitem(baris)
            row.setitem(kolom, 0)
    
    def get_sel(self, baris, kolom):
        """Melihat status sel (0/1)"""
        if 0 <= baris < self.baris and 0 <= kolom < self.kolom:
            row = self.grid.getitem(baris)
            return row.getitem(kolom)
        return 0  # Di luar grid dianggap mati
    
    def hitung_tetangga(self, baris, kolom):
        """Menghitung jumlah tetangga hidup (8 arah)"""
        jumlah = 0
        for i in range(-1, 2):  # -1, 0, 1
            for j in range(-1, 2):  # -1, 0, 1
                if i == 0 and j == 0:
                    continue  # Lewati sel sendiri
                jumlah += self.get_sel(baris + i, kolom + j)
        return jumlah
    
    def generasi_berikutnya(self):
        """Menghasilkan generasi baru berdasarkan 4 aturan"""
        # Buat grid baru
        grid_baru = GameOfLife(self.baris, self.kolom)
        
        # Terapkan aturan ke setiap sel
        for i in range(self.baris):
            for j in range(self.kolom):
                tetangga = self.hitung_tetangga(i, j)
                sel_saat_ini = self.get_sel(i, j)
                
                # ATURAN 1-4 dari dokumen!
                if sel_saat_ini == 1:  # Sel hidup
                    if tetangga in [2, 3]:  # Aturan 1: tetap hidup
                        grid_baru.set_hidup(i, j)
                    else:  # Aturan 2 & 3: mati (kesepian/overpopulasi)
                        grid_baru.set_mati(i, j)
                else:  # Sel mati
                    if tetangga == 3:  # Aturan 4: lahir
                        grid_baru.set_hidup(i, j)
        
        self.grid = grid_baru.grid
        return self
    
    def tampilkan(self):
        """Menampilkan grid di layar"""
        print("-" * (self.kolom * 2 + 1))
        for i in range(self.baris):
            baris_str = "|"
            for j in range(self.kolom):
                if self.get_sel(i, j) == 1:
                    baris_str += "█|"  # Sel hidup
                else:
                    baris_str += " |"  # Sel mati
            print(baris_str)
        print("-" * (self.kolom * 2 + 1))
    
    def simpan(self, filename, generasi_ke):
        """Menyimpan generasi ke file"""
        with open(filename, 'a') as f:
            f.write(f"\n=== GENERASI {generasi_ke} ===\n")
            for i in range(self.baris):
                baris_str = ""
                for j in range(self.kolom):
                    baris_str += "█" if self.get_sel(i, j) == 1 else "·"
                f.write(baris_str + "\n")
