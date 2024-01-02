from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from models.obat import Obat
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.uic import loadUi

class PopoupobatForm(QDialog):
    data_sent = pyqtSignal(dict)
    def __init__(self,parent=None):
        super(PopoupobatForm,self).__init__(parent)
        loadUi('views/cariobat.ui',self)
        self.TampilData()
        self.btnPilih.clicked.connect(self.send_data)
       

    def TampilData(self):
        data_obat = Obat.tampil_Obat()
        if data_obat:
            self.tblObat.setRowCount(0)
            for row_number,row_data in enumerate(data_obat):
                self.tblObat.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblObat.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    for row in range(self.tblObat.rowCount()):
                        for col in range(self.tblObat.columnCount()):
                            item = self.tblObat.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled) 

    def send_data(self):
        row = self.tblObat.currentRow()
        kodeObat = self.tblObat.item(row,0).text()
        namaObat = self.tblObat.item(row,1).text()
        hargaObat = self.tblObat.item(row,3).text()

        data = {"kodeObat": kodeObat, "namaObat": namaObat, "hargaObat": hargaObat}
        self.data_sent.emit(data)
        self.close()