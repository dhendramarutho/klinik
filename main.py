import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
from controllers.PasienController import PasienForm
from controllers.DokterController import DokterForm
from controllers.PeriksaController import PeriksaForm
from controllers.UserController import UserForm
from controllers.LoginController import LoginForm
from controllers.PenjualanController import PenjualanForm

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('views/main_windows.ui',self)
        self.showMaximized()
        # self.user = user
        # self.role = role

        self.actionPasien.triggered.connect(self.showPasienForm)
        self.actionDokter.triggered.connect(self.showDokterForm)
        self.actionPeriksa.triggered.connect(self.showPeriksaForm)
        self.actionUser.triggered.connect(self.showUserForm)
        self.actionLogin.triggered.connect(self.showLoginForm)
        self.actionPenjualan_Obat.triggered.connect(self.showFormPenjualan)
        self.showLoginForm()
        self.non_active_menu()

    def activate_menus(self,data):
        # Aktifkan menu sesuai dengan peran pengguna
        role = data["role"]
        if role == "admin":
            self.actionPasien.setEnabled(True)
            self.actionDokter.setEnabled(True)
            self.actionPeriksa.setEnabled(True)
            self.actionObat.setEnabled(True)
            self.actionUser.setEnabled(True)
            self.actionPenjualan_Obat.setEnabled(True)
            self.actionPembelian_Obat.setEnabled(True)
            self.actionData_Pasien.setEnabled(True)
            self.actionData_Dokter.setEnabled(True)
            self.actionData_Obat.setEnabled(True)
            self.actionLaporan_Pemeriksaan.setEnabled(True)
            self.actionPenjualan_Obat.setEnabled(True)
            self.actionLogin.setText("Logout")
        elif role == "dokter":
            self.actionPasien.setEnabled(False)
            self.actionDokter.setEnabled(False)
            self.actionPeriksa.setEnabled(True)
            self.actionObat.setEnabled(False)
            self.actionUser.setEnabled(False)
            self.actionPenjualan_Obat.setEnabled(False)
            self.actionPembelian_Obat.setEnabled(False)
            self.actionData_Pasien.setEnabled(False)
            self.actionData_Dokter.setEnabled(False)
            self.actionData_Obat.setEnabled(False)
            self.actionLaporan_Pemeriksaan.setEnabled(False)
            self.actionPenjualan_Obat.setEnabled(False)
            self.actionLogin.setText("Logout")
        elif role == "kasir":
            self.actionPasien.setEnabled(False)
            self.actionDokter.setEnabled(False)
            self.actionPeriksa.setEnabled(False)
            self.actionObat.setEnabled(False)
            self.actionUser.setEnabled(False)
            self.actionPenjualan_Obat.setEnabled(True)
            self.actionPembelian_Obat.setEnabled(True)
            self.actionData_Pasien.setEnabled(True)
            self.actionData_Dokter.setEnabled(False)
            self.actionData_Obat.setEnabled(True)
            self.actionLaporan_Pemeriksaan.setEnabled(True)
            self.actionPenjualan_Obat.setEnabled(True)
            self.actionLogin.setText("Logout")
        else:
            self.non_active_menu()

    def non_active_menu(self):
        self.actionPasien.setEnabled(False)
        self.actionDokter.setEnabled(False)
        self.actionPeriksa.setEnabled(False)
        self.actionObat.setEnabled(False)
        self.actionUser.setEnabled(False)
        self.actionPenjualan_Obat.setEnabled(False)
        self.actionPembelian_Obat.setEnabled(False)
        self.actionData_Pasien.setEnabled(False)
        self.actionData_Dokter.setEnabled(False)
        self.actionData_Obat.setEnabled(False)
        self.actionLaporan_Pemeriksaan.setEnabled(False)
        self.actionPenjualan_Obat.setEnabled(False)
        self.actionLogin.setEnabled(True)
        self.actionLogin.setText("Login")

    def showPasienForm(self):
        self.formPasien = PasienForm()
        self.formPasien.setModal(True)
        self.formPasien.show()

    def showDokterForm(self):
        self.formDokter = DokterForm()
        self.formPasien.setModal(True)
        self.formDokter.show()

    def showPeriksaForm(self):
        self.fromPeriksa = PeriksaForm()
        self.fromPeriksa.setModal(True)
        self.fromPeriksa.show()
    
    def showUserForm(self):
        self.formPasien = UserForm()
        self.formPasien.setModal(True)
        self.formPasien.show()

    def showLoginForm(self):
        self.non_active_menu()
        self.formLogin = LoginForm()
        self.formLogin.data_sent.connect(self.activate_menus)
        self.formLogin.setModal(True)
        self.formLogin.show()

        if self.actionLogin.text() == "Logut":
            self.non_active_menu()
    
    def showFormPenjualan(self):
        self.formPenjualan = PenjualanForm()
        self.formPenjualan.setModal(True)
        self.formPenjualan.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = MainMenu() 
    mainMenu.show()
    sys.exit(app.exec_())
   
