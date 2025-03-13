def breadth_search(_start, _goal, _graph):
    _open = [_start]
    _closed = []
    _count = 0

    while True:#_open != None:
        x = _open[0]
        ++_count
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
        x = _open[0]
        ++_count
        if x == _goal:
            return _count
            print("TRUE")
        else:
            _open.remove(x)
            _closed.append(x)
            for i in _graph[x]:
                if i not in _open and i not in _closed:
                    _open.insert(0,i)
            #print(_open[0])
    print("FALSE")
    return False

while True:
    try:
        N = int(input("Введите количество вершин: "))  # Например, N = 5
        break
    except:
        print("Вводимое значение должно быть числовым и целочисленным")
_graph = {0: []}
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