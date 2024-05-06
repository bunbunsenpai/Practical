INF = 9999999  # A large value representing infinity (for initialization)
V = 5  # Number of vertices in the graph

# Adjacency matrix representation of the weighted graph
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

# Initialize an array to track selected vertices (0 means not selected, 1 means selected)
selected = [0] * V

# Start with the first vertex (e.g., vertex 0)
selected[0] = True

print("Edge : Weight")
no_edge = 0  # Number of edges in the MST

while no_edge < V - 1:
    minimum = INF
    x, y = 0, 0

    # For every selected vertex, find the adjacent vertices and their weights
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j]:  # Not selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x, y = i, j

    print(f"{x} - {y}: {G[x][y]}")
    selected[y] = True
    no_edge += 1