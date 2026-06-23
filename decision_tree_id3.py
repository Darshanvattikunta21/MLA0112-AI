import math
from collections import Counter


def entropy(rows):
    counts = Counter(row["play"] for row in rows)
    total = len(rows)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def information_gain(rows, attribute):
    base_entropy = entropy(rows)
    total = len(rows)
    weighted_entropy = 0

    for value in {row[attribute] for row in rows}:
        subset = [row for row in rows if row[attribute] == value]
        weighted_entropy += (len(subset) / total) * entropy(subset)

    return base_entropy - weighted_entropy


def majority_label(rows):
    return Counter(row["play"] for row in rows).most_common(1)[0][0]


def id3(rows, attributes):
    labels = {row["play"] for row in rows}
    if len(labels) == 1:
        return labels.pop()
    if not attributes:
        return majority_label(rows)

    best_attribute = max(attributes, key=lambda attr: information_gain(rows, attr))
    tree = {best_attribute: {}}

    for value in sorted({row[best_attribute] for row in rows}):
        subset = [row for row in rows if row[best_attribute] == value]
        remaining = [attr for attr in attributes if attr != best_attribute]
        tree[best_attribute][value] = id3(subset, remaining)

    return tree


if __name__ == "__main__":
    dataset = [
        {"outlook": "sunny", "temperature": "hot", "humidity": "high", "wind": "weak", "play": "no"},
        {"outlook": "sunny", "temperature": "hot", "humidity": "high", "wind": "strong", "play": "no"},
        {"outlook": "overcast", "temperature": "hot", "humidity": "high", "wind": "weak", "play": "yes"},
        {"outlook": "rain", "temperature": "mild", "humidity": "high", "wind": "weak", "play": "yes"},
        {"outlook": "rain", "temperature": "cool", "humidity": "normal", "wind": "weak", "play": "yes"},
        {"outlook": "rain", "temperature": "cool", "humidity": "normal", "wind": "strong", "play": "no"},
        {"outlook": "overcast", "temperature": "cool", "humidity": "normal", "wind": "strong", "play": "yes"},
        {"outlook": "sunny", "temperature": "mild", "humidity": "high", "wind": "weak", "play": "no"},
        {"outlook": "sunny", "temperature": "cool", "humidity": "normal", "wind": "weak", "play": "yes"},
        {"outlook": "rain", "temperature": "mild", "humidity": "normal", "wind": "weak", "play": "yes"},
    ]

    attributes = ["outlook", "temperature", "humidity", "wind"]
    print("Entropy:", round(entropy(dataset), 3))
    for attribute in attributes:
        print(f"Gain({attribute}):", round(information_gain(dataset, attribute), 3))
    print("ID3 tree:", id3(dataset, attributes))
