# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_another.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(309, 271)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelHeader = QtWidgets.QLabel(Dialog)
        self.labelHeader.setObjectName("labelHeader")
        self.verticalLayout.addWidget(self.labelHeader)
        self.labelEntropy = QtWidgets.QLabel(Dialog)
        self.labelEntropy.setObjectName("labelEntropy")
        self.verticalLayout.addWidget(self.labelEntropy)
        self.labelLength = QtWidgets.QLabel(Dialog)
        self.labelLength.setObjectName("labelLength")
        self.verticalLayout.addWidget(self.labelLength)
        self.resultTable = QtWidgets.QTableWidget(Dialog)
        self.resultTable.setObjectName("tableView")
        # self.resultTable.horizontalHeader().setVisible(False)
        self.resultTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.resultTable)
        self.btnBack = QtWidgets.QPushButton(Dialog)
        self.btnBack.setObjectName("btnBack")
        self.verticalLayout.addWidget(self.btnBack)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelHeader.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Код </span></p></body></html>"))
        self.labelEntropy.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Значение энтропии для алфавита:</span></p></body></html>"))
        self.labelLength.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Средняя длина кодовых комбинаций: </span></p></body></html>"))
        self.btnBack.setText(_translate("Dialog", "Вернуться назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
