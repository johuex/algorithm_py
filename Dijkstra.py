# создаем три таблицы для данного алгоритма: сам граф, стоимости и родители
# граф с весами ребер
graph = dict()
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

#таблица стоимости
infinity = float("inf") #бесконечность в Python
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"]= infinity

#родители
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

processed = [] #список обработанных узлов

node = find_lowest_cost_node(costs)#находим узел с наим. стоим. среди необработанных
while node is not None: #если обработаны все узлы, то while прекращается
    cost = costs[node] #
    neighbors = graph[node] #
    for n in neighbors.keys(): #перебираем всех соседей узла
        new_cost = cost + neighbors[n] #2-е слагаемое: расстояние до сосед узла
        if costs[n] > new_cost: # если к соседу можно быстрее добраться через текущий узел
            costs[n] = new_cost #обновляем стоимость
            parents[n] = node # узел становится новым родителем для соседа
    processed.append(node) # помечаем узел как обработанный
    node = find_lowest_cost_node(costs) #найти след узел для обработки и повтор цикл

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: #перебор всех узлов
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            '''если этот узел с наим стоим из увиденных и не был обработан'''
            lowest_cost = cost # то он назначается новым узлом
            lowest_cost_node = node # с наим стоимостью
    return lowest_cost_node