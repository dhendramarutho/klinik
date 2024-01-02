from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from models.pasien import Pasien
from controllers.PopupDokterController import Popupdokterform
from laporan.lap_pasien import create_pasien_pdf

class PasienForm(QDialog):
    def __init__(self,parent=None):
        super(PasienForm,self).__init__(parent)
        loadUi('views/pasien.ui',self)
        self.TampilData()
        self.btnSimpan.clicked.connect(self.simpanData)
        self.btnEdit.clicked.connect(self.updateData)
        self.btnCetak.clicked.connect(self.generate_pdf)
        self.tblPasien.itemDoubleClicked.connect(self.handle_item_double_click)
        self.btnKeluar.clicked.connect(self.popup)

    def popup(self):
        self.fromPopdokter = Popupdokterform()
        self.fromPopdokter.data_sent.connect(self.handle_data_from_form2)  # Menghubungkan sinyal data_sent
        self.fromPopdokter.setModal(True)
        self.fromPopdokter.show()

    def handle_data_from_form2(self,data):
        self.txtKodePasien.setText(data)

    def TampilData(self):
        data_pasien = Pasien.tampil_pasien()
        if data_pasien:
            self.tblPasien.setRowCount(0)
            for row_number,row_data in enumerate(data_pasien):
                self.tblPasien.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblPasien.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    # Menonaktifkan semua baris yang ditampilkan
                    for row in range(self.tblPasien.rowCount()):
                        for col in range(self.tblPasien.columnCount()):
                            item = self.tblPasien.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled)


    def handle_item_double_click(self):
        row = self.tblPasien.currentRow()
        kodepasien = self.tblPasien.item(row,0).text()
        namapasien = self.tblPasien.item(row,1).text()
        alamat = self.tblPasien.item(row,2).text()
        jk = self.tblPasien.item(row,3).text()
        hp = self.tblPasien.item(row,4).text()

        self.txtKodePasien.setText(kodepasien)
        self.txtNamaPasien.setText(namapasien)
        self.txtAlamat.setText(alamat)
        self.txtHP.setText(hp)
        self.cmbJK.setCurrentText(jk)

    # def disable_all_rows(self):
    #     for row in range(self.tblPasien.rowCount()):
    #         for col in range(self.tblPasien.columnCount()):
    #             item = self.tblPasien.item(row, col)
    #             if item:
    #                 item.setFlags(item.flags() & Qt.ItemIsEnabled)

    def generate_pdf(self):
        data_pasien = Pasien.tampil_pasien()
        create_pasien_pdf(data_pasien)

    def kosong_form(self):
        self.txtKodePasien.setText('')
        self.txtKodePasien.setFocus()
        self.txtNamaPasien.setText('')
        self.txtAlamat.setText('')
        self.txtHP.setText('')
        self.cmbJK.setCurrentText('Pria')
    
    def simpanData(self):
        kode = self.txtKodePasien.text()
        nama = self.txtNamaPasien.text()
        alamat = self.txtAlamat.text()
        nohp = self.txtHP.text()
        jk = self.cmbJK.currentText()
        pasien = Pasien(kode,nama,alamat,jk,nohp)
        pasien.save()
        QMessageBox.information(self,'Success','Data Pasien berhasil disimpan..!!!')
        self.TampilData()
        self.kosong_form()

    def updateData(self):
        kode_lama = self.txtKodePasien.text()
        kode = self.txtKodePasien.text()
        nama = self.txtNamaPasien.text()
        alamat = self.txtAlamat.text()
        nohp = self.txtHP.text()
        jk = self.cmbJK.currentText()
        pasien = Pasien(kode,nama,alamat,jk,nohp)
        pasien.update(kode_lama)
        QMessageBox.information(self,'Success','Data Pasien berhasil dirubah..!!!')
        self.TampilData()

    def deleteData(self):
        kode_pasien = self.txtKodePasien.text()
        Pasien.delete(kode_pasien)
        QMessageBox.information(self,'Success','Data Pasien berhasil dihapus..!!!')
        self.TampilData()