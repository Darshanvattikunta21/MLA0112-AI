def train_linear_svm(samples, labels, epochs=20, learning_rate=0.01, penalty=1.0):
    weights = [0.0, 0.0]
    bias = 0.0

    for _ in range(epochs):
        for sample, label in zip(samples, labels):
            margin = label * (sum(x * w for x, w in zip(sample, weights)) + bias)
            if margin >= 1:
                weights = [w - learning_rate * (2 * w) for w in weights]
            else:
                weights = [
                    w - learning_rate * (2 * w - penalty * label * x)
                    for w, x in zip(weights, sample)
                ]
                bias += learning_rate * penalty * label

    return weights, bias


def predict(sample, weights, bias):
    score = sum(x * w for x, w in zip(sample, weights)) + bias
    return 1 if score >= 0 else -1


if __name__ == "__main__":
    data = [(1, 1), (2, 1), (2, 2), (6, 5), (7, 7), (8, 6)]
    labels = [-1, -1, -1, 1, 1, 1]
    weights, bias = train_linear_svm(data, labels)

    print("Weights:", [round(weight, 3) for weight in weights])
    print("Bias:", round(bias, 3))
    print("Prediction for (5, 5):", predict((5, 5), weights, bias))
