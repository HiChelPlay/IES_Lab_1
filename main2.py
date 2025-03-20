import sys

from PySide6.QtWidgets import QApplication, QDialog, QComboBox, QDateEdit, QMainWindow, QTableView, QVBoxLayout, \
    QWidget, QMessageBox, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import QDate, Qt, QModelIndex, QTimer, QThread, Signal, QObject
from PySide6.QtGui import QStandardItemModel, QStandardItem

from int import Ui_Dialog

from main import *

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

        self.ui.FindBreadth.clicked.connect(self.get_values)
        #self.ui.FindDepth.clicked.connect(self.get_values)

        # startData = int(self.ui.Start.data())
        # goalData = int(self.ui.Goal.data())






    def get_values(self):
        row_count = self.model.rowCount()
        col_count = self.model.columnCount()

        # Проходим по всем ячейкам и получаем их значения
        for row in range(row_count):
            for col in range(col_count):
                index = self.model.index(row, col)  # Получаем индекс ячейки
                value = int(self.model.data(index, Qt.DisplayRole))  # Получаем значение
                if value == 1:
                    main._graph[row].append(col)
        #print(main._graph)

        startData = int(self.ui.Start.data())
        goalData = int(self.ui.Goal.data())
        main.breadth_search(startData, goalData, main._graph)


    # def get_values(self):
    #     # Получаем количество строк и столбцов
    #     row_count = self.model.rowCount()
    #     col_count = self.model.columnCount()
    #
    #     # Проходим по всем ячейкам и получаем их значения
    #     for row in range(row_count):
    #         for col in range(col_count):
    #             index = self.model.index(row, col)  # Получаем индекс ячейки
    #             value = self.model.data(index, Qt.DisplayRole)  # Получаем значение
    #             print(f"Ячейка [{row}, {col}]: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())