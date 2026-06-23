import math
from collections import Counter


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn_predict(points, query, k=3):
    nearest = sorted(points, key=lambda item: distance(item[0], query))[:k]
    votes = Counter(label for _, label in nearest)
    return votes.most_common(1)[0][0], nearest


if __name__ == "__main__":
    data = [
        ((1, 2), "low"),
        ((2, 3), "low"),
        ((3, 3), "low"),
        ((6, 5), "high"),
        ((7, 7), "high"),
        ((8, 6), "high"),
    ]

    label, neighbors = knn_predict(data, (5, 5), k=3)
    print("Query point: (5, 5)")
    print("Nearest neighbors:", neighbors)
    print("Predicted class:", label)
