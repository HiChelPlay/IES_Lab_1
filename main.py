

#from PySide import *

from main2 import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec())

def breadth_search(_start, _goal, _graph):
    _open = [_start]
    _closed = []
    _count = 0

    while True:
        print(_open)
        x = _open[0]
        _count += 1
        if x == _goal:
            return _count
        else:
            _open.remove(x)
            _closed.append(x)
            for i in _graph[x]:
                if i not in _open and i not in _closed:
                    _open.append(i)
            #print(_open[0])
    return False

def depth_search(_start, _goal, _graph):
    _open = [_start]
    _closed = []
    _count = 0

    while True:#_open != None:
        print(_open)
        x = _open[0]
        _count += 1
        if x == _goal:
            return _count
        else:
            _open.remove(x)
            _closed.append(x)
            for i in _graph[x]:
                if i not in _open and i not in _closed:
                    _open.insert(0, i)
            #print(_open[0])
    return False

# def depth_search(_start, _goal, _graph):
#     _open = [_start]  # Стек вершин для обработки
#     _closed = set()   # Множество обработанных вершин
#     _count = 0        # Счетчик шагов
#
#     while _open:  # Пока стек не пуст
#         print("Открытый список:", _open)
#         x = _open.pop(0)  # Берем вершину из начала стека
#         _count += 1
#
#         if x == _goal:  # Если вершина - цель
#             return _count  # Возвращаем количество шагов
#
#         _closed.add(x)  # Добавляем вершину в закрытый список
#
#         # Добавляем всех потомков вершины x в начало стека
#         for neighbor in _graph[x]:
#             if neighbor not in _open and neighbor not in _closed:
#                 _open.insert(0, neighbor)  # Добавляем в начало стека
#
#     return False  # Цель не найдена

# while True:
#     try:
#         N = int(input("Введите количество вершин: "))  # Например, N = 5
#         break
#     except:
#         print("Вводимое значение должно быть числовым и целочисленным")
_graph = {0: [1,3], 1: [2,0],  2: [], 3: [4], 4: []}
# Создаем список смежности с динамическими списками
#_graph = {i: [] for i in range(N)}  # Создаем граф с N вершинами
#
# Заполнение графа
#for i in range(N):
#    while True:
#        try:
#            # Вводим смежные вершины для вершины i
#            neighbor = input(f"Введите смежную вершину для вершины {i} (или 'q' для завершения): ")
#            if neighbor.lower() == 'q':  # Завершаем ввод для текущей вершины
#                break
#            neighbor = int(neighbor)  # Преобразуем в число
#            if 0 <= neighbor < N:  # Проверяем, что вершина существует
#                _graph[i].append(neighbor)
#            else:
#                print(f"Ошибка: вершина {neighbor} не существует.")
#        except ValueError:
#            print("Ошибка: введите число или 'q' для завершения.")

# Запускаем поиск
start = int(input("Введите начальную вершину: "))  # Начальная вершина
goal = int(input("Введите целевую вершину: "))   # Целевая вершина

result = breadth_search(start, goal, _graph)

print("Поиск в ширину:")
print("Цель не найдена" if result == False else f"Цель найдена за {result} шагов")

result = depth_search(start, goal, _graph)

print("Поиск в глубину:")
print("Цель не найдена" if result == False else f"Цель найдена за {result} шагов")


#print(_graph)




