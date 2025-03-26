import sys

from PySide6.QtWidgets import QApplication, QDialog, QComboBox, QDateEdit, QMainWindow, QTableView, QVBoxLayout, \
    QWidget, QMessageBox, QAbstractItemView, QPushButton, QGridLayout
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import QDate, Qt, QModelIndex, QTimer, QThread, Signal, QObject
from PySide6.QtGui import QStandardItemModel, QStandardItem
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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
graph_for_paint = [[0 for i in range(10)] for i in range(10)]
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
        print(_open)
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

        # Создание места для отображения графа
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Установка фиксированного размера и позиции для canvas
        self.canvas.setFixedSize(500, 300)  # Фиксированный размер
        self.canvas.move(20, 20)  # Позиция (100, 300) относительно окна

        # Не добавляем canvas в layout, чтобы управлять его позицией вручную
        self.canvas.setParent(self)  # Устанавливаем окно как родителя для canvas

    def build_graph(self):
        # Получение данных из таблицы
        matrix = []
        for i in range(7):
            row = []
            for j in range(9):
                item = self.table.item(i, j)
                if item and item.text().isdigit():
                    row.append(int(item.text()))
                else:
                    row.append(0)  # Если ячейка пуста или содержит нечисловое значение
            matrix.append(row)

        # Создание ориентированного графа
        G = nx.DiGraph()

        # Добавление узлов и ребер на основе матрицы смежности
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    G.add_edge(i, j)  # Добавляем ребро с направлением от i к j

        # Определение уровней для каждого узла
        levels = {
            0: 0,  # Начальная вершина на уровне 0 (верхний уровень)
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            7: 4,
            8: 4,
            9: 5
        }

        # Применение multipartite_layout для размещения узлов по уровням
        pos = nx.multipartite_layout(G, subset_key="layer", align="vertical")

        # Очистка предыдущего графа и отрисовка нового
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Отрисовка графа с стрелками
        nx.draw(
            G,
            pos,
            ax=ax,
            with_labels=True,
            node_color='lightblue',
            edge_color='gray',
            arrows=True,  # Включаем стрелки
            arrowstyle='->',  # Стиль стрелок
            arrowsize=10  # Размер стрелок
        )
        self.canvas.draw()

    def load(self, index):
        row = index.row()
        col = self.ui.tableView.currentIndex().column()

        # Обновление данных в графе
        if col not in graph[row]:
            self.model.setData(self.model.index(row, col), 1)
            graph_for_paint[row][col] = 1
            graph[row].append(col)
        else:
            self.model.setData(self.model.index(row, col), 0)
            graph_for_paint[row][col] = 0  # Исправлено: значение должно быть 0
            del graph[row][graph[row].index(col)]

        self.ui.tableView.clearSelection()

        # Обновление графа
        self.update_graph()  # Вызов метода для обновления графа

    def update_graph(self):
        # Создание ориентированного графа
        G = nx.DiGraph()

        # Добавление узлов и ребер на основе матрицы смежности
        for i in range(len(graph_for_paint)):
            for j in range(len(graph_for_paint[i])):
                if graph_for_paint[i][j] == 1:
                    G.add_edge(i, j)  # Добавляем ребро с направлением от i к j

        # Определение уровней для каждого узла
        levels = {
            0: 0,  # Начальная вершина на уровне 0 (верхний уровень)
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            7: 4,
            8: 4,
            9: 5
        }

        # Назначение атрибута "layer" для каждого узла
        for node in G.nodes():
            G.nodes[node]["layer"] = levels.get(node, 0)  # По умолчанию уровень 0, если узел не найден в словаре

        # Применение multipartite_layout для размещения узлов по уровням
        pos = nx.multipartite_layout(G, subset_key="layer")

        # Ручное изменение координат для вертикального расположения
        for node in pos:
            x, y = pos[node]
            pos[node] = (y, -x)  # Меняем местами x и y, инвертируем y для вертикального расположения

        # Очистка предыдущего графа и отрисовка нового
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Отрисовка графа с стрелками
        nx.draw(
            G,
            pos,
            ax=ax,
            with_labels=True,
            node_color='lightblue',
            edge_color='gray',
            arrows=True,  # Включаем стрелки
            arrowstyle='->',  # Стиль стрелок
            arrowsize=10  # Размер стрелок
        )
        self.canvas.draw()

    def breadth(self):
        # try: #Добавление 1
            start = int(self.ui.lineEdit.text())
            end = int(self.ui.lineEdit_2.text())
            self.ui.lineEdit_4.setText(str(breadth_search(start, end, graph)))
            self.ui.lineEdit_3.setText(to_str(finish_breadth))
            finish_breadth.clear() #Изменение 1
        # except:
        #     QMessageBox.warning(self, "Ошибка", "Введены неверные значения начальной и конечной точки!")

    def deapth(self):
        try: #Добавление 2
            start = int(self.ui.lineEdit.text())
            end = int(self.ui.lineEdit_2.text())
            self.ui.lineEdit_6.setText(str(depth_search(start, end, graph)))
            self.ui.lineEdit_5.setText(to_str(finish_deapth))
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
        for i in range(len(graph_for_paint)):
            for j in range(len(graph_for_paint[i])):
                if graph_for_paint[i][j] == 1:
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