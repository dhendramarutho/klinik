import sqlite3
import bcrypt

class User():
    pathDB = 'databases\db_klinik.db'
    def __init__(self,username,password,name,role):
        self.username = username 
        self.password = password
        self.name = name
        self.role = role

    def tampil_user():
        try:
            conn = sqlite3.connect(User.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM user"
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
            conn =  sqlite3.connect(User.pathDB)
            curr = conn.cursor()
            # Hash kata sandi sebelum menyimpannya
            hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
            query = "INSERT INTO user (username,password,nama,role) VALUES (?,?,?,?)"
            curr.execute(query,(self.username,hashed_password,self.name,self.role))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close()