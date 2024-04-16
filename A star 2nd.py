import heapq

class GraphNode:
    def __init__(self, label, heuristic):
        self.label = label
        self.heuristic = heuristic
        self.edges = []
        self.parent = None

    def add_edge(self, neighbor, cost):
        self.edges.append((neighbor, cost))
        neighbor.parent = self

def astar(start, goal):
    open_list = [(start.heuristic, start)]
    closed_set = set()

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(start, goal)

        closed_set.add(current_node)

        for neighbor, cost in current_node.edges:
            if neighbor not in closed_set:
                total_cost = current_node.heuristic + cost
                heapq.heappush(open_list, (total_cost, neighbor))

    return None

def reconstruct_path(start, goal):
    path = []
    current_node = goal

    while current_node:
        path.append(current_node.label)
        current_node = getattr(current_node, 'parent', None)

    return path[::-1]

if __name__ == "__main__":
    S = GraphNode('S', 6)
    A = GraphNode('A', 4)
    B = GraphNode('B', 4)
    C = GraphNode('C', 4)
    D = GraphNode('D', 3.5)
    E = GraphNode('E', 1)
    F = GraphNode('F', 1)
    G = GraphNode('G', 0)

    S.add_edge(A, 2)
    S.add_edge(B, 3)
    A.add_edge(C, 3)
    B.add_edge(C, 1)
    B.add_edge(D, 3)
    C.add_edge(E, 3)
    C.add_edge(D, 1)
    D.add_edge(F, 2)
    E.add_edge(G, 2)
    F.add_edge(G, 1)

    S.parent = None

    path = astar( S, E)

    if path:
        print("Shortest path:", "->".join(path))
    else:
        print("No path found.")
