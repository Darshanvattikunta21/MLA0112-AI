import math
import random


def objective(x):
    return -(x - 4) ** 2 + 20


def simulated_annealing(start, temperature=10.0, cooling=0.85, iterations=30):
    random.seed(7)
    current = start
    best = current

    for _ in range(iterations):
        candidate = current + random.choice([-1, 1])
        delta = objective(candidate) - objective(current)
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current = candidate
        if objective(current) > objective(best):
            best = current
        temperature *= cooling

    return best, objective(best)


if __name__ == "__main__":
    best_point, best_value = simulated_annealing(start=-3)
    print("Best point:", best_point)
    print("Best value:", best_value)
