import sys
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)
angka = QWidget()
lb1 = QLabel(angka)
luas = QLineEdit()
luas.setStyleSheet("border : 3px solid black; font:bold; color:black; font-size:10px;")


def persegi():
    tampilan=QFormLayout(angka)
    m1=QLabel()
    m1.setText("Masukan Luas     :")
    tampilan.addRow(m1)
    tampilan.addRow(luas)

    hasil=QPushButton()
    hasil.setText("HASIL")
    hasil.setStyleSheet("font:bold; color:black; font-size:10px;")
    hasil.clicked.connect(hitung)
    tampilan.addRow(hasil)
  
    tampilan.addRow(lb1)

    angka.setGeometry(100,100,300,200)
    angka.setWindowTitle("PyQt LUAS PERSEGI")
    angka.setStyleSheet("background-image:#0000A0")
    angka.show()
    sys.exit(app.exec_())
def hitung():
    try:
        bil1=int(luas.text())
    except ValueError:
        lb1.setText("Inputan LUAS harus berupa angka!")
        lb1.setStyleSheet("font:bold; color:black; font-size:10px")
   
    else:
        hasil= bil1*bil1
        lb1.setText("LUAS PERSEGI ="+str(hasil))
        lb1.setStyleSheet("font:bold; color:black; font-size:10px;")


if __name__ == '__main__':
    persegi()
