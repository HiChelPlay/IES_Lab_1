import sys

from PySide6.QtWidgets import QApplication, QDialog, QComboBox, QDateEdit, QMainWindow, QTableView, QVBoxLayout, \
    QWidget, QMessageBox, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import QDate, Qt, QModelIndex, QTimer, QThread, Signal, QObject
from PySide6.QtGui import QStandardItemModel, QStandardItem
#import networkx as nx
#import matplotlib.pyplot as plt

from int import Ui_Dialog



graph = {0:[],
         1:[],
         2:[],
         3:[],
         4:[],
         5:[],
         6:[],
         7:[],
         8:[],
         9:[]}
grapgh_for_paint = [[0 for i in range(10)] for i in range(10)]
global finish_breadth
finish_breadth = []
global finish_deapth
finish_deapth = []

def to_str(list1):
    result = ""
    for i in range(len(list1) - 1):
        result += str(list1[i]) + "-"
    result += str(list1[-1])
    return result
def breadth_search(_start, _goal, _graph):
    _open = [_start]
    _closed = []
    _count = 1
    _ukaz = []
    _checkUkaz = _goal

    while True:
        x = _open[0]
        if x == _goal:
            while _checkUkaz != _start: #Добавил 3
                for i in range(len(_ukaz)):
                    if _checkUkaz in _ukaz[i]:
                        for j in _ukaz[i]:
                            if j not in finish_breadth:
                                finish_breadth.append(j)
                        _checkUkaz = finish_breadth[-1]
                        break
            finish_breadth.reverse()
            return _count
        else:
            _open.remove(x)
            _closed.append(x)
            for i in _graph[x]:
                if i not in _open and i not in _closed:
                    _ukaz.append([i,x])
                    _open.append(i)

        _count += 1
    return False

def depth_search(_start, _goal, _graph):
    _open = [_start]
    _closed = []
    _count = 1
    _ukaz = []
    _checkUkaz = _goal

    while True:
        x = _open[0]
        if x == _goal:
            while _checkUkaz != _start: #Добавил 4
                for i in range(len(_ukaz)):
                    if _checkUkaz in _ukaz[i]:
                        for j in _ukaz[i]:
                            if j not in finish_deapth:
                                finish_deapth.append(j)
                        _checkUkaz = finish_deapth[-1]
                        break
            finish_deapth.reverse()
            return _count
        else:
            _open.remove(x)
            _closed.append(x)
            _preOpen = []
            for i in _graph[x]:
                if i not in _open and i not in _closed:
                    _ukaz.append([i, x])
                    _preOpen.append(i)
            _preOpen.reverse()
            for i in _preOpen:
                _open.insert(0, i)
        _count += 1
    return False

class Menu(QDialog):
    def __init__(self):
        super(Menu, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableView.clicked.connect(self.load)
        self.ui.FindBreadth.clicked.connect(self.breadth)
        self.ui.FindDepth.clicked.connect(self.deapth)
        self.ui.pushButton.clicked.connect(self.clear)

        self.model = QStandardItemModel()

        _matrixRange = 10

        for row in range(_matrixRange):
            for col in range(_matrixRange):
                item = QStandardItem('0')
                self.model.setItem(row, col, item)

        self.ui.tableView.setModel(self.model)

        for col in range(_matrixRange):
            self.model.setHeaderData(col, Qt.Horizontal, col)
            self.model.setHeaderData(col, Qt.Vertical, col)

        self.ui.tableView.resizeColumnsToContents()

    def load(self, index):
        row = index.row()
        col = self.ui.tableView.currentIndex().column()
        if col not in graph[row]:
            self.model.setData(self.model.index(row, col), 1)
            grapgh_for_paint[row][col] = 1
            graph[row].append(col)
        else:
            self.model.setData(self.model.index(row, col), 0)
            grapgh_for_paint[row][col] = 1
            del graph[row][graph[row].index(col)]
        self.ui.tableView.clearSelection()

    def breadth(self):
        try: #Добавление 1
            start = int(self.ui.Start.text())
            end = int(self.ui.Goal.text())
            self.ui.StepsBreadth.setText(str(breadth_search(start, end, graph)))
            self.ui.WayBreadth.setText(to_str(finish_breadth))
            finish_breadth.clear() #Изменение 1
        except:
            QMessageBox.warning(self, "Ошибка", "Введены неверные значения начальной и конечной точки!")

    def deapth(self):
        try: #Добавление 2
            start = int(self.ui.Start.text())
            end = int(self.ui.Goal.text())
            self.ui.StepsDepth.setText(str(depth_search(start, end, graph)))
            self.ui.WayDepth.setText(to_str(finish_deapth))
            finish_deapth.clear()
        except:
            QMessageBox.warning(self, "Ошибка", "Введены неверные значения начальной и конечной точки!")

    def clear(self):
        finish_deapth = []
        finish_breadth = []
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_6.setText("")

    def paint(self):
        G = nx.Graph()

        # Добавление вершин и рёбер на основе матрицы смежности
        for i in range(len(grapgh_for_paint)):
            for j in range(len(grapgh_for_paint[i])):
                if grapgh_for_paint[i][j] == 1:
                    G.add_edge(i, j)

        # Визуализация графа
        pos = nx.spring_layout(G)  # Позиционирование вершин
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)

        # Отображение графа
        plt.show()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())