from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from models.user import User

class UserForm(QDialog):
    def __init__(self,parent=None):
        super(UserForm,self).__init__(parent)
        loadUi('views/user.ui',self)
        self.TampilData()
        self.btnSimpan.clicked.connect(self.Simpan)
        self.btnKeluar.clicked.connect(self.keluar)

    def TampilData(self):
            data_user = User.tampil_user()
            if data_user:
                self.tblUser.setRowCount(0)
                for row_number,row_data in enumerate(data_user):
                    self.tblUser.insertRow(row_number)
                    for column_number,data in enumerate(row_data):
                        self.tblUser.setItem(row_number,column_number,
                                            QTableWidgetItem(str(data)))
                        for row in range(self.tblUser.rowCount()):
                            for col in range(self.tblUser.columnCount()):
                                item = self.tblUser.item(row, col)
                                if item:
                                    item.setFlags(item.flags() & Qt.ItemIsEnabled)

    def Simpan(self):
        username = self.txtUserName.text()
        password = self.txtPassword.text()
        nama = self.txtName.text()
        role = self.cmbRole.currentText()
        user = User(username,password,nama,role)
        user.save()
        QMessageBox.information(self,'Success','Data User berhasil disimpan..!!!')
        self.TampilData()

    def keluar(self):
        self.close()