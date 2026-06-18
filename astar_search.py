from heapq import heappop, heappush


def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def a_star_search(graph, heuristics, start, goal):
    open_set = []
    heappush(open_set, (heuristics[start], 0, start))

    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        _, current_cost, current = heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current), current_cost

        for neighbor, edge_cost in graph.get(current, []):
            new_cost = cost_so_far[current] + edge_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                heappush(open_set, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    return None, float("inf")


if __name__ == "__main__":
    sample_graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2), ("E", 5)],
        "C": [("E", 1)],
        "D": [("G", 3)],
        "E": [("G", 2)],
        "G": [],
    }

    sample_heuristics = {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 1,
        "E": 1,
        "G": 0,
    }

    path, cost = a_star_search(sample_graph, sample_heuristics, "A", "G")
    print("A* path:", path)
    print("Total cost:", cost)
