import sqlite3

class Obat():
    pathDB = 'databases\db_klinik.db'

    def __init__(self,kode,nama,jumlah,harga,stok):
        self.kode = kode 
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
        self.stok = stok


    def tampil_Obat():
        try:
            conn = sqlite3.connect(Obat.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM Obat"
            curr.execute(query)
            data_pasien = curr.fetchall()
            return data_pasien
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()

    def save(self):
        try:
            conn =  sqlite3.connect(Obat.pathDB)
            curr = conn.cursor()
            query = "INSERT INTO Obat (kode,nama,jumlah,harga,stok) VALUES (?,?,?,?,?)"
            curr.execute(query,(self.kode,self.nama,self.jumlah,self.harga,self.stok))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close()

    def update(self,kode_lama):
        try:
            conn =  sqlite3.connect(Obat.pathDB)
            curr = conn.cursor()
            query = "UPDATE Obat SET kode = ?,nama = ?,jumlah = ?,jk = ?,harga = ? WHERE kode = ?"
            curr.execute(query,(self.kode,self.nama,self.jumlah,self.stok,self.harga,kode_lama))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 

    @staticmethod
    def delete(kode):
        try:
            conn =  sqlite3.connect(Obat.pathDB)
            curr = conn.cursor()
            query = "DELETE FROM Obat WHERE kode = ?"
            curr.execute(query,(kode,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 