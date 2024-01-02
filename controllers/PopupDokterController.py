from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from models.dokter import Dokter
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.uic import loadUi

class Popupdokterform(QDialog):
    data_sent = pyqtSignal(dict)
    def __init__(self,parent=None):
        super(Popupdokterform,self).__init__(parent)
        loadUi('views/caridokter.ui',self)
        self.TampilData()
        self.btnPilih.clicked.connect(self.send_data)
       

    def TampilData(self):
        data_dokter = Dokter.tampil_dokter()
        if data_dokter:
            self.tblDokter.setRowCount(0)
            for row_number,row_data in enumerate(data_dokter):
                self.tblDokter.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblDokter.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    for row in range(self.tblDokter.rowCount()):
                        for col in range(self.tblDokter.columnCount()):
                            item = self.tblDokter.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled) 

    def send_data(self):
        row = self.tblDokter.currentRow()
        kodedokter = self.tblDokter.item(row,0).text()
        namadokter = self.tblDokter.item(row,1).text()
        data = {"kodedokter": kodedokter, "namadokter": namadokter}
        self.data_sent.emit(data)
        self.close()