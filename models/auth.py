import sqlite3
import bcrypt

class Auth():
    pathDB = 'databases\db_klinik.db'
    def __init__(self):
        pass

    def authenticate(self,username,password):
        conn = None
        curr = None
        try:
            conn = sqlite3.connect(Auth.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM user WHERE username = ?"
            curr.execute(query, (username,))
            user_data = curr.fetchone()
            if user_data:
                stored_password = self.get_stored_password(username)
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    return user_data[1], user_data[3]  # Mengembalikan username dan role jika otentikasi berhasil
        except sqlite3.Error as e:
            print("Error:", e)
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        return None
    
    def get_stored_password(self, username):
        try:
            conn = sqlite3.connect(Auth.pathDB)
            curr = conn.cursor()
            query = "SELECT password FROM user WHERE username = ?"
            curr.execute(query, (username,))
            stored_password = curr.fetchone()[0]
            return stored_password
        except sqlite3.Error as e:
            print("Error:", e)
        finally:
            curr.close()
            conn.close()
        return None