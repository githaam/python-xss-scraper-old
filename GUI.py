"""
    GUI PYQT 5: CATATAN

    GANTI JADI PySimpleGUI?


"""

import sys
import program
from PyQt5.QtWidgets import * #QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import * #QIcon
from PyQt5.QtCore import * #pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'sXSS Checker'
        self.left = 450
        self.top = 250
        self.width = 500
        self.height = 197
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.boxInput()
        #self.tablePayload()
        self.listChecked()
        #self.bar()
        #self.loading()
        self.result()

        # Add box layout, add table to box layout
        #and add box layout to widget
        self.layout = QGridLayout()
        self.layout.addLayout(self.fBox,1,1)
        #self.layout.addWidget(self.listPayload,1,2)
        self.layout.addWidget(self.listURL,1,2)
        #self.layout.addWidget(self.progress,2,1,2,2)
        self.layout.addWidget(self.payload,2,1,2,2)
        self.layout.addWidget(self.out1,4,1,4,2)
        self.setLayout(self.layout)

        # Show widget
        self.show()


    #1
    def boxInput(self):
        self.verBox = QVBoxLayout()

        self.lab1 = QLabel("URL :")
        self.in1 = QLineEdit()
        self.b1 = QPushButton("Scan")

        self.verBox.addWidget(self.in1)
        self.verBox.addWidget(self.b1)

        self.fBox = QFormLayout()
        self.fBox.addRow(self.lab1, self.verBox)

        self.b1.clicked.connect(self.scan)

    #2
    def tablePayload(self):
       # Create table
        self.listPayload = QTableWidget()
        self.listPayload.setColumnCount(1)
        #self.listPayload.move(0,0)

    #3
    def listChecked(self):
        self.listURL = QTableWidget()
        self.listURL.setRowCount(3) #LIST YANG DI KANAN
        self.listURL.setColumnCount(1)
        self.listURL.move(0,0)
        h1 = "URL :"

        header = self.listURL.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.listURL.setHorizontalHeaderLabels(['URL(s) Scanned'])

    #4
    def result(self):
        self.payload = QLineEdit("Pattern yang ditemukan")
        self.payload.setAlignment(Qt.AlignCenter)
        self.payload.setReadOnly(1)
        self.out1 = QLineEdit("Hasil")
        self.out1.setAlignment(Qt.AlignCenter)
        self.out1.setReadOnly(1)

    """
    def bar(self):
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0,0,300,25)
        self.progress.move(0,30)


    def loading(self):
        totalPatt = program.findPattern()

        self.completed = 0

        while self.completed < totalPatt:
            self.completed += 1/totalPatt #sampe sini
            self.progress.setValue(self.completed)
    """

    @pyqtSlot()
    #def on_click(self):
    #    print("\n")
    #    for currentQTableWidgetItem in self.listPayload.selectedItems():
    #        print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def scan(self):
        target = self.in1.text()
        hasilAkhir, pattern, scanned = program.main(target)

        #urlScanned = []
        #urlScanned = scanned

        for i in range(len(scanned)):
            self.listURL.setItem(i, 0, QTableWidgetItem(scanned[i]))
        self.out1.setText(hasilAkhir)
        self.payload.setText(pattern)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
