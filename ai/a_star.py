from bisect import insort_left
from collections import defaultdict


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, pt1):
        return self.x == pt1.x and self.y == pt1.y

    def __lt__(self, pt1):
        return self.x < pt1.x and self.y < pt1.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, pt1):
        return Point(self.x+pt1.x, self.y+pt1.y)

    def __repr__(self):
        return f"{self.x} {self.y}"

    def manhattan_h(self, pt1):
        return abs(pt1.x-self.x) + abs(pt1.y-self.y)


NEIGHBOR_COST = 1

# Moves = [UP, RIGHT, DOWN, LEFT]
MOVES = [
    Point(0, -1),
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0)
]


def _is_wall(grid, neighbor):
    return grid[neighbor.x][neighbor.y] == "%"


def _return_inf():
    return float("INF")


def _get_next_node(open_set, f_score):
    for _, point in f_score:
        if point in open_set:
            return point


def _reconstruc_path(came_from, current):
    final_path = [current]

    while current in came_from.keys():
        current = came_from[current]
        final_path.insert(0, current)

    return final_path


def a_star(pacman_pos, food_pos, grid):
    open_set = set([pacman_pos])
    closed_set = set()

    g_score = defaultdict(_return_inf)
    g_score[pacman_pos] = 0

    # f_score = [(g+h, point), ...]
    f_score = [(food_pos.manhattan_h(pacman_pos), pacman_pos)]

    path = dict()

    while open_set:
        current = _get_next_node(open_set, f_score)

        if current == food_pos:
            return _reconstruc_path(path, current)

        open_set.remove(current)
        closed_set.add(current)

        for move in MOVES:
            neighbor = move + current

            if neighbor in closed_set or _is_wall(grid, neighbor):
                continue

            tentative_g_score = g_score[current] + NEIGHBOR_COST

            if tentative_g_score < g_score[neighbor]:
                path[neighbor] = current
                g_score[neighbor] = tentative_g_score
                # Insert the neighbor in the right position in sorted f_score
                new_f_score = g_score[neighbor] + food_pos.manhattan_h(neighbor)
                insort_left(f_score, (new_f_score, neighbor))

                if neighbor not in open_set:
                    open_set.add(neighbor)

    return "FAIL"


def main():
    pacman_pos = Point(*[int(pos) for pos in input().split()])
    food_pos = Point(*[int(pos) for pos in input().split()])
    rows, columns = [int(length) for length in input().split()]

    grid = [input() for _ in range(rows)]

    path = a_star(pacman_pos, food_pos, grid)
    print(len(path)-1)
    print(*path, sep="\n")


if __name__ == "__main__":
    main()
