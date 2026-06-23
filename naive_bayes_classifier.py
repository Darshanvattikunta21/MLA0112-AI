from collections import Counter, defaultdict


class NaiveBayes:
    def fit(self, rows, labels):
        self.labels = sorted(set(labels))
        self.label_counts = Counter(labels)
        self.feature_counts = defaultdict(Counter)
        self.feature_values = defaultdict(set)

        for row, label in zip(rows, labels):
            for feature, value in row.items():
                self.feature_counts[(label, feature)][value] += 1
                self.feature_values[feature].add(value)

    def predict(self, row):
        total = sum(self.label_counts.values())
        scores = {}

        for label in self.labels:
            score = self.label_counts[label] / total
            for feature, value in row.items():
                values = len(self.feature_values[feature])
                count = self.feature_counts[(label, feature)][value]
                score *= (count + 1) / (self.label_counts[label] + values)
            scores[label] = score

        return max(scores, key=scores.get), scores


if __name__ == "__main__":
    training_rows = [
        {"weather": "sunny", "temp": "hot"},
        {"weather": "sunny", "temp": "mild"},
        {"weather": "rainy", "temp": "cool"},
        {"weather": "rainy", "temp": "mild"},
        {"weather": "overcast", "temp": "hot"},
    ]
    training_labels = ["no", "no", "yes", "yes", "yes"]

    model = NaiveBayes()
    model.fit(training_rows, training_labels)
    prediction, scores = model.predict({"weather": "rainy", "temp": "mild"})

    print("Prediction:", prediction)
    print("Scores:", {label: round(score, 4) for label, score in scores.items()})
