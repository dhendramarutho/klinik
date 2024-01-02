import sqlite3

class Dokter():
    pathDB = 'databases\db_klinik.db'

    def __init__(self,kode,nama,alamat,nohp,jenis):
        self.kode = kode 
        self.nama = nama
        self.alamat = alamat
        self.nohp = nohp
        self.jenis = jenis


    def tampil_dokter():
        try:
            conn = sqlite3.connect(Dokter.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM dokter"
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
            conn =  sqlite3.connect(Dokter.pathDB)
            curr = conn.cursor()
            query = "INSERT INTO dokter (kode,nama,alamat,nohp,jenis) VALUES (?,?,?,?,?)"
            curr.execute(query,(self.kode,self.nama,self.alamat,self.nohp,self.jenis))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close()

    def update(self,kode_lama):
        try:
            conn =  sqlite3.connect(Dokter.pathDB)
            curr = conn.cursor()
            query = "UPDATE dokter SET kode = ?,nama = ?,alamat = ?,jk = ?,nohp = ? WHERE kode = ?"
            curr.execute(query,(self.kode,self.nama,self.alamat,self.jenis,self.nohp,kode_lama))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 

    @staticmethod
    def delete(kode):
        try:
            conn =  sqlite3.connect(Dokter.pathDB)
            curr = conn.cursor()
            query = "DELETE FROM dokter WHERE kode = ?"
            curr.execute(query,(kode,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 