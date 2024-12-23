
import heapq
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'C': 5, 'E': 2},
    'C': {'F': 8},
    'D': {'B': 2, 'E': 6},
    'E': {'F': 3},
    'F': {}
}

def dijkstra(graph, start):
    
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]  # (mesafe, düğüm)
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths, previous_nodes


start_node = 'A'
shortest_paths, previous_nodes = dijkstra(graph, start_node)

def print_shortest_path(previous_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    return path

print("Başlangıç düğümü:", start_node)
for node in graph:
    if node != start_node:
        path = print_shortest_path(previous_nodes, start_node, node)
        print(f"{start_node} -> {node}: En kısa yol: {path}, Mesafe: {shortest_paths[node]}")