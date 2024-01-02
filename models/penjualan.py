import sqlite3

class Penjualan():
    pathDB = 'databases\db_klinik.db'

    def __init__(self,tanggal,total,keterangan,obat_list):
        self.tanggal = tanggal
        self.total = total
        self.keterangan = keterangan
        self.obat_list = obat_list

    def simpan_ke_database(self):
        try:
            conn = sqlite3.connect(self.pathDB)
            cursor = conn.cursor()
            
            tanggal = self.tanggal.strftime('%Y-%m-%d')
            cursor.execute("INSERT INTO penjualan (tanggal, keterangan, total) VALUES (?, ?, ?)",
                        (tanggal, self.keterangan, self.total))
            jual_id = cursor.lastrowid
            for obat in self.obat_list:
                kode_obat, nama_obat, jumlah,harga,subtotal = obat
                cursor.execute("INSERT INTO penjualan_detil (id_jual,kode_obat,nama_obat,jumlah,harga,subtotal) VALUES (?, ?, ?, ?, ?, ?)",
                                (jual_id, kode_obat, nama_obat, jumlah, harga, subtotal))
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            conn.commit()
            conn.close()