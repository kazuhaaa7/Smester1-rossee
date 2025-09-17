#!/usr/bin/env python3
"""
graph_nim.py
Build graph from NIM and run BFS/DFS.
Usage examples:
  python graph_nim.py --nim 222410101100
  python graph_nim.py --nim 123456 --connect_same
  python graph_nim.py --nim 222410101100 --visualize
"""

import argparse
from collections import deque, defaultdict

DEFAULT_NIM = "252410101090"

def make_suffix(i):
    # A, B, ..., Z, A0, B0, ... simple fallback for >26 length
    if i < 26:
        return chr(ord('A') + i)
    else:
        return chr(ord('A') + (i % 26)) + str(i // 26)

def build_graph(nim, connect_same_digit=False):
    nodes = [f"{nim[i]}{make_suffix(i)}" for i in range(len(nim))]
    graph = {node: [] for node in nodes}

    # chain (neighbor) connections
    for i, node in enumerate(nodes):
        if i > 0:
            graph[node].append(nodes[i-1])
        if i < len(nodes) - 1:
            graph[node].append(nodes[i+1])

    # ensure undirected: add reverse links
    for u in list(graph.keys()):
        for v in list(graph[u]):
            if u not in graph[v]:
                graph[v].append(u)

    # optional: connect all nodes with same digit
    if connect_same_digit:
        groups = defaultdict(list)
        for node in nodes:
            digit = node[:-1]  # '2' from '2A'
            groups[digit].append(node)
        for group in groups.values():
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    a, b = group[i], group[j]
                    if b not in graph[a]:
                        graph[a].append(b)
                    if a not in graph[b]:
                        graph[b].append(a)

    # sort neighbor lists for deterministic output
    for k in graph:
        graph[k] = sorted(graph[k])
    return graph, nodes

def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited.append(start)
    order = []
    while queue:
        m = queue.popleft()
        order.append(m)
        for neigh in graph.get(m, []):
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
    return order

def dfs_recursive(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    if start not in visited:
        visited.add(start)
        order.append(start)
        for neigh in graph.get(start, []):
            if neigh not in visited:
                dfs_recursive(graph, neigh, visited, order)
    return order

def dfs_iterative(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()  # LIFO
        if node not in visited:
            visited.add(node)
            order.append(node)
            # push neighbors in reverse order to mimic recursive left-to-right
            for neigh in reversed(graph.get(node, [])):
                if neigh not in visited:
                    stack.append(neigh)
    return order

def print_graph(graph):
    print("Adjacency list:")
    for k in sorted(graph.keys()):
        print(f"  {k} : {graph[k]}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nim', default=DEFAULT_NIM, help='NIM string (digits only)')
    parser.add_argument('--connect_same', action='store_true', help='Connect nodes with same digit')
    parser.add_argument('--start_index', type=int, default=0, help='Start node index (0-based). Default 0 (xA)')
    parser.add_argument('--visualize', action='store_true', help='Try to visualize (requires networkx & matplotlib)')
    args = parser.parse_args()

    nim = args.nim.strip()
    if not nim.isdigit():
        raise SystemExit("NIM harus berisi digit saja (0-9).")

    graph, nodes = build_graph(nim, connect_same_digit=args.connect_same)

    # validate start index
    if args.start_index < 0 or args.start_index >= len(nodes):
        raise SystemExit("start_index di luar jangkauan node.")
    start = nodes[args.start_index]

    print(f"NIM: {nim}")
    print(f"Nodes: {nodes}")
    print_graph(graph)
    print()
    print("Start node:", start)
    print("BFS order :", bfs(graph, start))
    print("DFS order (recursive) :", dfs_recursive(graph, start))
    print("DFS order (iterative) :", dfs_iterative(graph, start))

    if args.visualize:
        try:
            import networkx as nx
            import matplotlib.pyplot as plt
            G = nx.Graph()
            for u in graph:
                G.add_node(u)
                for v in graph[u]:
                    G.add_edge(u, v)
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True)
            plt.show()
        except Exception as e:
            print("Visualize gagal: pastikan networkx & matplotlib terpasang. Error:", e)

if __name__ == "__main__":
    main()
