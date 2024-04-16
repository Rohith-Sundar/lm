import heapq

class PuzzleState:
    def __init__(self, board, parent=None, depth=0):
        self.board = board
        self.parent = parent
        self.depth = depth

    def __lt__(self, other):
        return self.depth + self.h() < other.depth + other.h()

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

    def is_goal(self):
        goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        return self.board == goal_state

    def h(self):
        goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        return sum(1 for i in range(3) for j in range(3) if self.board[i][j] != goal_state[i][j])

    def get_successors(self):
        successors = []
        zero_i, zero_j = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0][0]

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in moves:
            new_i, new_j = zero_i + move[0], zero_j + move[1]

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_board = [row.copy() for row in self.board]
                new_board[zero_i][zero_j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[zero_i][zero_j]
                successors.append(PuzzleState(new_board, self, self.depth + 1))

        return successors


def a_star(initial_state):
    open_list = [initial_state]
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            return current_state 

        closed_set.add(current_state)

        successors = current_state.get_successors()

        for successor in successors:
            if successor in closed_set:
                continue

            if successor not in open_list or successor.depth < open_list[open_list.index(successor)].depth:
                heapq.heappush(open_list, successor)

    return None  


def print_solution(solution_state):
    path = []
    while solution_state:
        path.append(solution_state.board)
        solution_state = solution_state.parent

    for i in range(len(path) - 1, -1, -1):
        print("Step", len(path) - i - 1)
        for row in path[i]:
            print(row)
        print()


if __name__ == "__main__":
    initial_state = PuzzleState([[1, 0, 3], [8, 2, 4], [7, 6, 5]])

    solution_state = a_star(initial_state)

    if solution_state:
        print("Solution found!")
        print_solution(solution_state)
    else:
        print("No solution found.")
