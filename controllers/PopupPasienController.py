from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from models.pasien import Pasien
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.uic import loadUi

class Popuppasienform(QDialog):
    data_sent = pyqtSignal(dict)
    def __init__(self,parent=None):
        super(Popuppasienform,self).__init__(parent)
        loadUi('views/caripasien.ui',self)
        self.TampilData()
        self.btnPilih.clicked.connect(self.send_data)
       

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

    def send_data(self):
        row = self.tblPasien.currentRow()
        kodepasien = self.tblPasien.item(row,0).text()
        namapasien = self.tblPasien.item(row,1).text()
        data = {"kodepasien": kodepasien, "namapasien": namapasien}
        self.data_sent.emit(data)
        self.close()