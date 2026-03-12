import heapq


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    prioryti_queue = [(0, start)]
    while prioryti_queue:
        #извлекаем вершину с наименьшим расстоянием очереди
        cost, vertex = heapq.heappop(prioryti_queue) #выбирает самы еверхринй элемент в куче

        if (cost > distances[vertex]):
            continue
        for neighbour, weight in graph[vertex].items():
            d= cost + weight
            if d < distances[neighbour]:
                distances[neighbour] = d
                heapq.heappush(prioryti_queue, (d, neighbour))
    return distances


graph = {
    'A': {'B': 1, 'C': 2, 'D': 3},
    'B': {'C': 1, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 2, 'E': 3},
    'D': {'B': 1, 'C': 2, 'E': 3},
    'E': {'B': 1, 'C': 2, 'D': 3},

}

result = dijkstra(graph, 'A')
print("Оптивамльное расстояние до вершины:")
for vertex, distance in result.items():
    print(vertex, distance)

