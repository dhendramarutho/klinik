import sqlite3

class Pasien():
    pathDB = 'databases\db_klinik.db'
    def __init__(self,kode,nama,alamat,jk,no_hp):
        self.kode = kode 
        self.nama = nama
        self.alamat = alamat
        self.jk = jk 
        self.no_hp = no_hp

    def tampil_pasien():
        try:
            conn = sqlite3.connect(Pasien.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM pasien"
            curr.execute(query)
            data_pasien = curr.fetchall()
            return data_pasien
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()

    def tampil_pasien_by_kode(kode):
        try:
            conn = sqlite3.connect(Pasien.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM pasien where kode = ?"
            curr.execute(query)
            data_pasien = curr.fetchall()
            return data_pasien
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()

    def search_pasien(kata_kunci):
        try:
            conn = sqlite3.connect(Pasien.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM pasien where kode LIKE '%" + kata_kunci + "%' OR nama LIKE '%" + kata_kunci + "%' OR alamat LIKE '%" + kata_kunci + "%'  "
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
            conn =  sqlite3.connect(Pasien.pathDB)
            curr = conn.cursor()
            query = "INSERT INTO pasien (kode,nama,alamat,jk,nohp) VALUES (?,?,?,?,?)"
            curr.execute(query,(self.kode,self.nama,self.alamat,self.jk,self.no_hp))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close()

    def update(self,kode_lama):
        try:
            conn =  sqlite3.connect(Pasien.pathDB)
            curr = conn.cursor()
            query = "UPDATE pasien SET kode = ?,nama = ?,alamat = ?,jk = ?,nohp = ? WHERE kode = ?"
            curr.execute(query,(self.kode,self.nama,self.alamat,self.jk,self.no_hp,kode_lama))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 

    @staticmethod
    def delete(kode):
        try:
            conn =  sqlite3.connect(Pasien.pathDB)
            curr = conn.cursor()
            query = "DELETE FROM pasien WHERE kode = ?"
            curr.execute(query,(kode,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 