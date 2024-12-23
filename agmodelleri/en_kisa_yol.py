import heapq

# Düğüm ve kenar ağırlıklarını tanımlıyoruz
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'C': 5, 'E': 2},
    'C': {'F': 8},
    'D': {'E': 6},
    'E': {'F': 3},
    'F': {}
}

def dijkstra(graph, start):
    # Tüm düğümler için başlangıçta sonsuz mesafe tanımlanır
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Başlangıç düğümünün mesafesi 0 olarak tanımlanır
    priority_queue = [(0, start)]  # Öncelik sırasına göre işlenecek düğümler

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Daha kısa bir yol bulunduysa işlenir
        if current_distance > distances[current_node]:
            continue

        # Komşu düğümler ve mesafeler işlenir
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Daha kısa bir yol bulunduysa güncellenir
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# A düğümünden tüm düğümlere olan en kısa yolları hesaplıyoruz
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
