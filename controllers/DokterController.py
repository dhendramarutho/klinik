from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from models.dokter import Dokter

class DokterForm(QDialog):
    def __init__(self,parent=None):
        super(DokterForm,self).__init__(parent)
        loadUi('views/dokter.ui',self)
        self.TampilData()
        # self.btnSimpan.clicked.connect(self.simpanData)
        # self.btnEdit.clicked.connect(self.updateData)
        # self.btnCetak.clicked.connect(self.generate_pdf)
        # self.tblPasien.itemDoubleClicked.connect(self.handle_item_double_click)
        self.btnKeluar.clicked.connect(self.keluar)

    def TampilData(self):
        data_pasien = Dokter.tampil_dokter()
        if data_pasien:
            self.tblDokter.setRowCount(0)
            for row_number,row_data in enumerate(data_pasien):
                self.tblDokter.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblDokter.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    for row in range(self.tblDokter.rowCount()):
                        for col in range(self.tblDokter.columnCount()):
                            item = self.tblDokter.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled)

    def keluar(self):
        self.close()