# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineProba = QtWidgets.QLineEdit(self.centralwidget)
        self.lineProba.setInputMask("")
        self.lineProba.setText("")
        self.lineProba.setClearButtonEnabled(True)
        self.lineProba.setObjectName("lineProba")
        self.verticalLayout.addWidget(self.lineProba)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineLetters = QtWidgets.QLineEdit(self.centralwidget)
        self.lineLetters.setClearButtonEnabled(True)
        self.lineLetters.setObjectName("lineLetters")
        self.verticalLayout.addWidget(self.lineLetters)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.radioShannon = QtWidgets.QRadioButton(self.centralwidget)
        self.radioShannon.setObjectName("radioShannon")
        self.verticalLayout.addWidget(self.radioShannon)
        self.radioHuffman = QtWidgets.QRadioButton(self.centralwidget)
        self.radioHuffman.setObjectName("radioHuffman")
        self.verticalLayout.addWidget(self.radioHuffman)
        self.btnCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnCode.setObjectName("pushCode")
        self.verticalLayout.addWidget(self.btnCode)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelEntropy = QtWidgets.QLabel(self.centralwidget)
        self.labelEntropy.setObjectName("labelEntropy")
        self.verticalLayout_2.addWidget(self.labelEntropy)
        self.labelLength = QtWidgets.QLabel(self.centralwidget)
        self.labelLength.setObjectName("labelLength")
        self.verticalLayout_2.addWidget(self.labelLength)
        self.resultTable = QtWidgets.QTableWidget(self.centralwidget)
        self.resultTable.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.resultTable)
        self.btnVisual = QtWidgets.QPushButton(self.centralwidget)
        self.btnVisual.setObjectName("btnVisual")
        self.verticalLayout_2.addWidget(self.btnVisual)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Префиксное кодирование</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Введите частотности появления букв алфавита (через пробел):</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Введите буквы алфавита через пробел (опционально):</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Выберите метод кодирования:</span></p></body></html>"))
        self.radioShannon.setText(_translate("MainWindow", "метод Шеннона-Фано"))
        self.radioHuffman.setText(_translate("MainWindow", "метод Хаффмана"))
        self.btnCode.setText(_translate("MainWindow", "Закодировать"))
        self.labelEntropy.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Значение энтропии для алфавита:</span></p></body></html>"))
        self.labelLength.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Средняя длина кодовых комбинаций: </span></p></body></html>"))
        self.btnVisual.setText(_translate("MainWindow", "Показать визуализацию решения"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
