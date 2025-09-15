from collections import deque

# Graph adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': ['H', 'I'],
    'G': [],
    'H': [],
    'I': []
}

goal = 'I'

# -------------------------------
# BFS
# -------------------------------
def bfs(start, goal):
    visited = set()
    queue = deque([[start]])  # simpan path
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None


# -------------------------------
# DFS
# -------------------------------
def dfs(start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    node = path[-1]
    if node == goal:
        return path
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            new_path = dfs(start, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None


# -------------------------------
# Depth-Limited Search (DLS)
# -------------------------------
def dls(node, goal, limit, path=None):
    if path is None:
        path = [node]
    if node == goal:
        return path
    if limit <= 0:
        return None
    for neighbor in graph[node]:
        new_path = dls(neighbor, goal, limit-1, path + [neighbor])
        if new_path:
            return new_path
    return None


# -------------------------------
# Iterative Deepening DFS (IDDFS)
# -------------------------------
def iddfs(start, goal, max_depth):
    for depth in range(max_depth+1):
        path = dls(start, goal, depth)
        if path:
            return path
    return None


# -------------------------------
# Testing
# -------------------------------
print("BFS Path:", bfs('A', goal))
print("DFS Path:", dfs('A', goal))
print("DLS Path (limit=2):", dls('A', goal, 2))   # gagal karena limit kecil
print("DLS Path (limit=4):", dls('A', goal, 4))   # berhasil
print("IDDFS Path (max_depth=4):", iddfs('A', goal, 4))

