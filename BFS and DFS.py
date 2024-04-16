from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start, end):
        visited = set()
        queue = deque()
        queue.append((start, [start]))

        while queue:
            node, path = queue.popleft()

            if node == end:
                print("Path found:", ' -> '.join(map(str, path)))
                return

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        print("Path does not exist.")

    def dfs(self, start, end):
        visited = set()
        stack = [(start, [start])]

        while stack:
            node, path = stack.pop()

            if node == end:
                print("Path found:", ' -> '.join(map(str, path)))
                return

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

        print("Path does not exist.")

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(4, 0)
g.add_edge(5, 0)
g.add_edge(5, 1)

source = int(input("Enter the source node: "))
destination = int(input("Enter the destination node: "))

print(f"BFS from {source} to {destination}:")
g.bfs(source, destination)

print(f"DFS from {source} to {destination}:")
g.dfs(source, destination)
