from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt,pyqtSignal
from models.auth import Auth

class LoginForm(QDialog):
    data_sent = pyqtSignal(dict)
    def __init__(self,parent=None):
        super(LoginForm,self).__init__(parent)
        loadUi('views/login.ui',self)
        self.btnLogin.clicked.connect(self.CekAuth)
        self.btnBatal.clicked.connect(self.keluar)
        self.auth = Auth()

    def CekAuth(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        user, role = self.auth.authenticate(username, password) or ("","")
        if user:
            data = {"user": user, "role": role}
            self.data_sent.emit(data)
            self.close()
        else:
            print("gagal")
            QMessageBox.warning(self,'Warning','User atau Password anda Salah...!!!')
            # self.close()

    def keluar(self):
        pass