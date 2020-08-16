# -*- encoding: utf-8 -*-
import sys
from GUI import design_main, design_another
from prefixCoding import AlphabetCoding
from prefixCoding.AlphabetCoding import sorting_dict, entropy
from PyQt5 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow, design_main.Ui_MainWindow):
    """Главное окно с выбором параметров кодирования"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(650, 300, 500, 500)
        self.setWindowTitle('Префиксное кодирование')
        self.setWindowIcon(QtGui.QIcon(r'resources\app_icon.png'))
        # По умолчанию метод кодирования не определен
        self.code_method = None
        # Кнопки выбора метода кодирования
        self.radioShannon.toggled.connect(self.set_method)
        self.radioHuffman.toggled.connect(self.set_method)
        # Кнопка кодирования (также открывающая новое окно)
        self.btnCode.clicked.connect(self.code_button)

    def set_method(self):
        """Выбор метода кодирования"""
        sender = self.sender()
        self.code_method = sender.text()

    def code_button(self):
        # Если пользователь по ошибке ввел вместо цифр какие-то другие символы
        try:
            frequencies = [float(i) for i in self.lineProba.text().split()]
        except ValueError:
            WarningWindow('Неправильный формат ввода для частотностей!').run()
            return
        letters = self.lineLetters.text().split()
        # Если пользователь не ввел частотности
        if len(frequencies) == 0:
            WarningWindow('Вы не ввели частотности появления букв!').run()
            return
        # Случай несоответствия числа введенных частотностей и букв
        if len(frequencies) != len(letters) and len(letters) != 0:
            WarningWindow('Число частотностей и букв не совпадает!').run()
            return
        # Случай неопределенности метода кодирования
        if self.code_method is None:
            WarningWindow('Вы не выбрали метод кодирования!').run()
            return
        # Если пользователь не ввел буквы алфавита, переменная letters принимает значение None, т.к. классы из
        # AlphabetCoding должны принимать None, если буквы не определены
        if len(letters) == 0:
            letters = None
        self.w = ResultWindow(frequencies, letters, self.code_method)
        # Новое окно имеет те же геометрические параметры, что и основное
        self.w.setGeometry(self.geometry())
        self.w.show()


class ResultWindow(QtWidgets.QDialog, design_another.Ui_Dialog):
    """Окно с результатами кодирования"""
    def __init__(self, frequencies, letters, method):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Префиксное кодирование')
        self.setWindowIcon(QtGui.QIcon(r'resources\app_icon.png'))
        # Инициализация параметров
        self.frequencies = frequencies
        self.letters = letters
        self.method = method
        # Кнопка "Назад"
        self.btnBack.clicked.connect(self.close)
        self.main_func()

    def main_func(self):
        self.labelHeader.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; '
                                 'font-weight:600;\">Код ' + self.method[6:] + '</span></p></body></html>')
        self.labelEntropy.setText(f'<html><head/><body><p><span style=\" font-size:10pt;\">Значение энтропии для '
                                  f'алфавита: {entropy(self.frequencies)}</span></p></body></html>')
        if self.method == "метод Шеннона-Фано":
            alph = AlphabetCoding.ShannonFano(self.frequencies, self.letters)
            alph.coding(sorting_dict(alph.probabilities))
        else:
            alph = AlphabetCoding.Huffman(self.frequencies, self.letters)
            alph.coding(alph.build_huffman_tree())
        self.labelLength.setText(f'<html><head/><body><p><span style=\" font-size:10pt;\">Средняя длина кодовых '
                                 f'комбинаций: {alph.mean_length()}</span></p></body></html>')
        # Создаем таблицу с результатами кодирования
        data = []
        for i in alph.probabilities:
            row = [i, str(alph.probabilities[i]), alph.coded_alphabet[i]]
            data.append(row)
        self.resultTable.setRowCount(len(data))
        self.resultTable.setColumnCount(3)
        self.resultTable.setHorizontalHeaderLabels(['Буква', 'Частотность', 'Код'])
        for i in range(len(data)):
            for j in range(3):
                self.resultTable.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j]))


class WarningWindow(QtWidgets.QMessageBox):
    """Окно ошибки"""
    def __init__(self, warning_text):
        super().__init__()
        self.warning_text = warning_text
        self.setWindowTitle('Внимание!')
        self.setText(self.warning_text)
        self.setIcon(QtWidgets.QMessageBox.Warning)

    def run(self):
        self.exec_()


def run():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == '__main__':
    run()

# TODO: сделать .exe файл
# TODO: Сделать визуализацию решения
# TODO: Сделать базу, хранящую закодированные алфавиты
# TODO: Создать репозиторий на GitHub
