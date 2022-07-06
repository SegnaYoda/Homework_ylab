"""Задача после второй лекций.

Программа для вычисления кратчайшего пути для почтальона.
"""


class Graph(object):
    """Класс описывает структуру графа всех точек для посещения."""

    def __init__(self, input_data):
        """Входящими данными является список всех координат точек."""
        self.input_data = input_data
        self.init_graph = {}    # инициализации графа
        for node in self.input_data:
            self.init_graph[str(node)] = {}
        # подсчет расстояний между точками
        self.init_graph = self.generator_init_graph(self.input_data,
                                                    self.init_graph)
        # перевод в str для удобства хранения
        self.nodes = [str(i) for i in input_data]
        # Метод construct_graph обеспечивает симметричность графа
        self.graph = self.construct_graph(self.nodes, self.init_graph)
        self.node_is_visited = {}
        for node in self.nodes:
            self.node_is_visited[node] = False

    def generator_init_graph(self, input_data, init_graph):
        """Генратор графа с расчетом расстояний между узлами."""
        if len(input_data) > 1:
            point_1 = input_data[0]
            input_data = input_data[1:]
            for point_2 in input_data:
                init_graph[str(point_1)][str(point_2)] = (((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)**0.5)
            return self.generator_init_graph(input_data, init_graph)
        return init_graph

    def construct_graph(self, nodes, init_graph):
        """Этот метод обеспечивает симметричность графа.

        Т.е., если существует путь от узла A к B
        со значением D, должен быть путь от узла B
        к узлу A со значением D.
        """
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) is False:
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        """Возвращает узлы графа."""
        return self.nodes

    def get_outgoing_edges(self, node):
        """Возвращает соседей узла."""
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) is not False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        """Возвращает значение ребра между двумя узлами."""
        return self.graph[node1][node2]

    def switch_visited(self, node):
        """Переключатель.

        Переключает отметку о посещении узла при итерации и поиска в глубину.
        """
        self.node_is_visited[node] = not self.node_is_visited[node]
        return self.node_is_visited[node]

    def check_visited(self, node):
        """Проверет отметку о посещении узла."""
        return self.node_is_visited[node]


class PostmansRoute:
    """Класс подсчета для вычисления кратчайшего пути для почтальона."""

    def __init__(self, graph):
        """Передаем объект класса Graph."""
        self.graph = graph

    def postmans_route(self, start_node, list_nodes, path, list_result):
        """Поиск в глубину по графу.

        Возвращает список возможных маршрутов,
        передает этот список для офомрления согласно задания.
        """
        self.graph.switch_visited(start_node)    # помечаем узел как visited
        path.append(start_node)
        if len(path) == len(list_nodes):
            list_result.append(path.copy())  # список всех возможных маршрутов
        neighbors = graph.get_outgoing_edges(start_node)  # соседи узла
        for neighbor in neighbors:
            if not graph.check_visited(neighbor):
                self.postmans_route(neighbor, list_nodes, path, list_result)
        path.remove(start_node)
        graph.switch_visited(start_node)  # помечаем узел как not visited
        return self.output_result(list_result)

    def output_result(self, result_list):
        """Представление результата к примеру оформления.

        Возвращает словарь с оформленным представлением маршрута(ключ),
        общую длину маршрута (значение) и значением кратчайшего пути.
        """
        shortest_route_value = []
        dict_road = {}
        for i in result_list:
            route_value = 0
            key_list = []
            for j in range(len(i)):
                if route_value == 0:
                    key_list += [i[-len(i) + j]]
                value_vs_node = graph.value(i[-len(i) + j], i[-len(i) + j + 1])
                route_value += value_vs_node
                key_list += [i[-len(i) + j + 1] + str([route_value])]
            dict_road[str(" -> ".join(key_list))] = route_value
            shortest_route_value.append(route_value)
            shortest_route_value = sorted(shortest_route_value)
        return dict_road, shortest_route_value[0]


# Блок ввода точек для посещения

# Варианты набора точек
# (0, 1), (4, 1), (7, 2), (5, 5), (1, 4), (10, 2)
# (0, 2), (5, 2), (6, 6), (2, 5), (8, 3)

# Либо выберите вариант для ручного ввода
input_data = [(0, 2), (5, 2), (6, 6), (2, 5), (8, 3)]

"""
# 2-ой вариант для построчного ввода
print("Пожалуйста, введите координаты точек.")
print("Почтовое отделение укажите первым в списке.")
input_data = []
for i in range(int(input("Введите количество точек: "))):
    a = input("Координаты точки через пробел: ").split(' ')
    a = (int(a[0]), int(a[1]))
    input_data.append(a)"""

graph = Graph(input_data)
postman = PostmansRoute(graph)
result_route_list, result_value_route = postman.postmans_route(str(input_data[0]), graph.get_nodes(), [], [])

for i in result_route_list:  # вывод результатов поиска
    if result_route_list[i] == result_value_route:
        print(i + " =", result_value_route)
