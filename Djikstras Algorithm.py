import sys

def Djikstras_Algorithm(graph, start_node):
    node_count = len(graph)
    shortest_distances = [sys.maxsize] * node_count
    included_in_tree = [False] * node_count

    
    shortest_distances[start_node] = 0

    for _ in range(node_count):
        current_node = select_node_with_minimum_distance(shortest_distances, included_in_tree, node_count)
        included_in_tree[current_node] = True

        for adjacent_node in range(node_count):
            if not included_in_tree[adjacent_node] and graph[current_node][adjacent_node] and \
               shortest_distances[current_node] != sys.maxsize and \
               shortest_distances[current_node] + graph[current_node][adjacent_node] < shortest_distances[adjacent_node]:
                shortest_distances[adjacent_node] = shortest_distances[current_node] + graph[current_node][adjacent_node]

    display_results(shortest_distances)

def select_node_with_minimum_distance(distances, visited, node_count):
    min_value = sys.maxsize
    min_node_index = -1

    for i in range(node_count):
        if not visited[i] and distances[i] < min_value:
            min_value = distances[i]
            min_node_index = i

    return min_node_index

def display_results(distances):
    print("Node \tShortest Distance from Start Node")
    for i in range(len(distances)):
        print(f"{i} \t\t {distances[i]}")

# Example
graph_example = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

Djikstras_Algorithm(graph_example, 0)
