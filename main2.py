import sys

from PySide6.QtWidgets import QApplication, QDialog, QComboBox, QDateEdit, QMainWindow, QTableView, QVBoxLayout, \
    QWidget, QMessageBox, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import QDate, Qt, QModelIndex, QTimer, QThread, Signal, QObject
from PySide6.QtGui import QStandardItemModel, QStandardItem

from int import Ui_Dialog

class Menu(QDialog):
    def __init__(self):
        super(Menu, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Создаем модель данных
        self.model = QStandardItemModel()

        # Заполняем модель данными


        _matrixRange = 10

        for row in range(_matrixRange):
            for col in range(_matrixRange):
                item = QStandardItem('0') #f"Item {row},{col}"
                self.model.setItem(row, col, item)
        # Устанавливаем модель в TableView
        self.ui.tableView.setModel(self.model)

        # self.model.setHeaderData(0, Qt.Vertical, "0")  # Пример для первой строки
        # self.model.setHeaderData(0, Qt.Horizontal, "0")  # Пример для первого столбца
        for col in range(_matrixRange):
            self.model.setHeaderData(col, Qt.Horizontal, col)
            self.model.setHeaderData(col, Qt.Vertical, col)

        # # Переопределяем заголовки строк и столбцов для нумерации с 0
        # self.model.setHeaderData(0, Qt.Vertical, "0")  # Пример для первой строки
        # self.model.setHeaderData(0, Qt.Horizontal, "0")  # Пример для первого столбца

        # Автоматическая подгонка ширины колонок
        self.ui.tableView.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())