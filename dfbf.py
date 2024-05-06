def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  # Print the visited vertex
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)

# Example graph
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

dfs(graph, 'A')

from collections import deque

def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  # Print the visited vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph (same as before)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')