import heapq

def dijkstra(graph, start):
    # Priority queue (min-heap)
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip outdated entries
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example: small India-like road network
graph = {
    "Hyderabad": [("Bangalore", 570), ("Chennai", 630)],
    "Bangalore": [("Hyderabad", 570), ("Chennai", 350), ("Mumbai", 980)],
    "Chennai": [("Hyderabad", 630), ("Bangalore", 350)],
    "Mumbai": [("Bangalore", 980)]
}

start_city = "Hyderabad"
distances = dijkstra(graph, start_city)

print("Shortest distances from", start_city)
for city, dist in distances.items():
    print(city, ":", dist)