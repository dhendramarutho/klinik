from tools.pdf import PDF
from PyQt5.QtWidgets import QMessageBox

def create_pasien_pdf(data):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # Header tabel
    pdf.set_fill_color(200, 200, 200)
    pdf.cell(40, 10, 'Kode', 1, 0, 'C', 1)
    pdf.cell(50, 10, 'Nama', 1, 0, 'C', 1)
    pdf.cell(40, 10, 'Alamat', 1, 0, 'C', 1)
    pdf.cell(30, 10, 'No. HP', 1, 0, 'C', 1)
    pdf.cell(30, 10, 'Jenis Kelamin', 1, 1, 'C', 1)

    # Isi data dari daftar mahasiswa
    for row_data in data:
        pdf.cell(40, 10, str(row_data[0]), 1, 0, 'C')
        pdf.cell(50, 10, str(row_data[1]), 1, 0, 'C')
        pdf.cell(40, 10, str(row_data[2]), 1, 0, 'C')
        pdf.cell(30, 10, str(row_data[3]), 1, 0, 'C')
        pdf.cell(30, 10, str(row_data[4]), 1, 1, 'C')

    pdf_file = 'laporan/laporan_pasien.pdf'
    pdf.output(pdf_file)
    QMessageBox.information(None, 'Success', 'Laporan PDF berhasil dibuat.')
