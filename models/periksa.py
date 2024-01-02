import sqlite3

class Periksa():
    pathDB = 'databases\db_klinik.db'

    def __init__(self,tanggal,kode_pasien,kode_dokter,keluhan,total_biaya,obat_list):
        self.tanggal = tanggal
        self.kode_pasien = kode_pasien
        self.kode_dokter = kode_dokter
        self.keluhan = keluhan
        self.total_biaya = total_biaya
        self.obat_list = obat_list

    def simpan_ke_database(self):
        try:
            conn = sqlite3.connect(self.pathDB)
            cursor = conn.cursor()
            # Simpan data periksa ke tabel periksa
            tanggal = self.tanggal.strftime('%Y-%m-%d')
            cursor.execute("INSERT INTO periksa (tanggal, kode_pasien, kode_dokter, keluhan, total_biaya) VALUES (?, ?, ?, ?, ?)",
                        (tanggal, self.kode_pasien, self.kode_dokter, self.keluhan, self.total_biaya))
            periksa_id = cursor.lastrowid  # Dapatkan ID periksa yang baru saja disimpan

            # Simpan data obat ke tabel obat untuk setiap obat dalam obat_list
            for obat in self.obat_list:
                kode_obat, nama_obat, jumlah,harga,subtotal = obat  # Membuka elemen tupel
                cursor.execute("INSERT INTO periksa_detil (kode_periksa,kode_obat,nama_obat,jumlah,harga,subtotal) VALUES (?, ?, ?, ?, ?, ?)",
                                (periksa_id, kode_obat, nama_obat, jumlah, harga, subtotal))
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            conn.commit()
            conn.close()