import math
from collections import Counter


def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def information_gain(parent_labels, child_groups):
    parent_entropy = entropy(parent_labels)
    total = len(parent_labels)
    child_entropy = sum((len(group) / total) * entropy(group) for group in child_groups)
    return parent_entropy - child_entropy


if __name__ == "__main__":
    parent = ["yes", "yes", "yes", "yes", "no", "no"]
    sunny = ["yes", "no", "no"]
    rainy = ["yes", "yes", "yes"]

    print("Parent entropy:", round(entropy(parent), 3))
    print("Sunny entropy:", round(entropy(sunny), 3))
    print("Rainy entropy:", round(entropy(rainy), 3))
    print("Information gain:", round(information_gain(parent, [sunny, rainy]), 3))
