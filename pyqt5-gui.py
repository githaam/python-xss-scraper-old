"""
    GUI PYQT 5
"""

import sys
import testing
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
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.boxInput()
        self.tablePayload()
        self.listChecked()
        self.result()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QGridLayout()
        self.layout.addLayout(self.fBox,1,1)
        self.layout.addWidget(self.listPayload,1,2)
        self.layout.addWidget(self.listURL,2,1)
        self.layout.addWidget(self.out1,2,2)
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
        #self.listPayload.setRowCount(8)
        #self.listPayload.setItem(0,0, QTableWidgetItem("Cell (1)"))
        self.listPayload.move(0,0)

        # table selection change
        #self.listPayload.doubleClicked.connect(self.on_click)

    #3
    def listChecked(self):
        self.listURL = QTableWidget()
        self.listURL.setRowCount(3)
        self.listURL.setColumnCount(1)
        self.listURL.setItem(0,0, QTableWidgetItem("Cell (1)"))
        self.listURL.setItem(1,0, QTableWidgetItem("Cell (2)"))
        self.listURL.setItem(2,0, QTableWidgetItem("Cell (3)"))
        self.listURL.move(0,0)

    #4
    def result(self):
        self.out1 = QLineEdit("Hasil")
        self.out1.setAlignment(Qt.AlignCenter)
        self.out1.setReadOnly(1)

    @pyqtSlot()
    #def on_click(self):
    #    print("\n")
    #    for currentQTableWidgetItem in self.listPayload.selectedItems():
    #        print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def scan(self):
        target = self.in1.text()
        hasil = testing.tolong(target)

        self.listPayload.setRowCount(len(target))

        self.out1.setText(hasil)
        for i in range(len(target)):
            self.listPayload.setItem(i,0, QTableWidgetItem(target[i]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
