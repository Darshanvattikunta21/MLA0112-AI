def objective(x):
    return -(x - 3) ** 2 + 10


def hill_climb(start, step=1):
    current = start
    path = [current]

    while True:
        neighbors = [current - step, current + step]
        best_neighbor = max(neighbors, key=objective)
        if objective(best_neighbor) <= objective(current):
            return current, objective(current), path
        current = best_neighbor
        path.append(current)


if __name__ == "__main__":
    point, value, path = hill_climb(start=-2)
    print("Path:", path)
    print("Best point:", point)
    print("Objective value:", value)
