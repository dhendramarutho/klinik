from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt,QDate
from controllers.PopupDokterController import Popupdokterform
from controllers.PopupPasienController import Popuppasienform
from controllers.PopupObatController import PopoupobatForm
from models.periksa import Periksa


class PeriksaForm(QDialog):
    def __init__(self,parent=None):
        super(PeriksaForm,self).__init__(parent)
        loadUi('views/periksa.ui',self)
        current_date = QDate.currentDate()
        self.obat_list = []
        self.total_biaya = 0.0
        self.dtpTanggal.setDate(current_date)
        self.btnCariDokter.clicked.connect(self.popupDokter)
        self.btnCariPasien.clicked.connect(self.popupPasien)
        self.btnTambahObat.clicked.connect(self.popupObat)
        self.btnInsertObat.clicked.connect(self.insertTable)
        self.btnSimpan.clicked.connect(self.saveDatabase)

    def popupDokter(self):
        self.formDokter = Popupdokterform()
        self.formDokter.data_sent.connect(self.handle_data_from_popUpdokter)  # Menghubungkan sinyal data_sent
        self.formDokter.setModal(True)
        self.formDokter.show()

    def handle_data_from_popUpdokter(self,data):
        self.txtKodeDokter.setText(data["kodedokter"])
        self.txtNamaDokter.setText(data["namadokter"])


    def popupPasien(self):
        self.formPasien = Popuppasienform()
        self.formPasien.data_sent.connect(self.handle_data_from_popUppasien)  # Menghubungkan sinyal data_sent
        self.formPasien.setModal(True)
        self.formPasien.show()

    def handle_data_from_popUppasien(self,data):
        self.txtKodePasien.setText(data["kodepasien"])
        self.txtNamaPasien.setText(data["namapasien"])


    def popupObat(self):
        self.formObatpopUp = PopoupobatForm()
        self.formObatpopUp.data_sent.connect(self.handle_data_from_popUpObat)  # Menghubungkan sinyal data_sent
        self.formObatpopUp.setModal(True)
        self.formObatpopUp.show()

    def handle_data_from_popUpObat(self,data):
        self.txtKodeObat.setText(data["kodeObat"])
        self.txtNamaObat.setText(data["namaObat"])
        self.txtHargaObat.setText(data["hargaObat"])
        self.txtJml.setFocus()

    def clearText(self):
        self.txtKodeObat.clear()
        self.txtNamaObat.clear()
        self.txtHargaObat.clear()
        self.txtJml.clear()

    def insertTable(self):
        kode =  self.txtKodeObat.text()
        nama =  self.txtNamaObat.text()
        jumlah = float(self.txtJml.text())
        harga = float(self.txtHargaObat.text())
        subtotal = float(self.txtJml.text()) * float(self.txtHargaObat.text())

        for row in range(self.tblObat.rowCount()):
            item = self.tblObat.item(row, 0)
            if item and item.text() == kode:
                current_jumlah = float(self.tblObat.item(row, 2).text())
                new_jumlah = current_jumlah + float(jumlah)
                new_subtotal = new_jumlah * float(harga)
                self.tblObat.setItem(row, 2, QTableWidgetItem(str(new_jumlah)))
                self.tblObat.setItem(row, 4, QTableWidgetItem(str(new_subtotal)))
                self.obat_list[row] = (kode,nama, new_jumlah,harga,new_subtotal)
                self.hitungTotal()
                self.clearText()
                return

        row_position = self.tblObat.rowCount()
        self.tblObat.insertRow(row_position)
        self.tblObat.setItem(row_position, 0, QTableWidgetItem(kode))
        self.tblObat.setItem(row_position, 1, QTableWidgetItem(nama))
        self.tblObat.setItem(row_position, 2, QTableWidgetItem(str(jumlah)))
        self.tblObat.setItem(row_position, 3, QTableWidgetItem(str(harga)))
        self.tblObat.setItem(row_position, 4, QTableWidgetItem(str(subtotal)))
        self.obat_list.append((kode,nama,jumlah,harga,subtotal))
        self.hitungTotal()
        self.clearText()
        

    def hitungTotal(self):
        self.total_biaya = 0.0
        for row in range(self.tblObat.rowCount()):
            subtotal_item = float(self.tblObat.item(row, 4).text())
            self.total_biaya += subtotal_item
        self.txtTotalBiaya.setText(str(self.total_biaya))

    def saveDatabase(self):
        tanggal = self.dtpTanggal.date().toPyDate()
        kodePasien = self.txtKodePasien.text()
        kodeDokter = self.txtKodeDokter.text()
        keluhan = self.txtKeluhan.toPlainText()
        total_biaya = self.txtTotalBiaya.text()
        detil_obat = self.obat_list
        periksa = Periksa(tanggal,kodePasien,kodeDokter,keluhan,total_biaya,detil_obat)
        periksa.simpan_ke_database()
        QMessageBox.information(self,'Success','Data Periksa berhasil disimpan..!!!')



    