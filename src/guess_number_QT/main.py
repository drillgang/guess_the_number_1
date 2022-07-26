from PyQt5 import QtCore, QtGui, QtWidgets
import random, sys

class Ui_MainWindow(object):
    
    """
    init window
    :return: None
    """
    
    def setupUi(self, MainWindow):
        self.nm=random.randint(-1000,1000)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(180, 126)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(0,0,0);font: 15pt \"Microsoft Sans Serif\";")
        self.label.setText("Число выбрано")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("font: 15pt \"Microsoft Sans Serif\";")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def check(self):
        
        """
        function with click button
        :return: None
        """
        
        print(self.nm)
        val=self.lineEdit.text()
        if val:
            val=int(val)
            if val==self.nm:
                self.label.setText(' ')
                msg=QtWidgets.QMessageBox.question(None,'Error','Вы угадали, хотите повторить?', QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
                if msg==QtWidgets.QMessageBox.Yes:
                    self.label.setText("Число выбрано")
                    self.lineEdit.clear()
                    self.nm=random.randint(-1000,1000)
                else:
                    self.lineEdit.clear()
                    sys.exit()
            elif val>self.nm:
                self.lineEdit.clear()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("  ")
                msg.setText("Вы ошиблись, выбранное число меньше, попробуйте еще раз")
                msg.exec()
            elif val<self.nm:
                self.lineEdit.clear()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("  ")
                msg.setText("Вы ошиблись, выбранное число больше, попробуйте еще раз")
                msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("  ")
            msg.setText("Попробуйте еще раз")
            msg.exec()

    def retranslateUi(self, MainWindow):
        
        """
        func with names
        :return: None
        """
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guess the number"))
        self.pushButton.setText(_translate("MainWindow", "Проверить"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Win = QtWidgets.QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(Win)
    Win.show()
    app.exec()