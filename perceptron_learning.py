def step(value):
    return 1 if value >= 0 else 0


def train_perceptron(samples, labels, epochs=6, learning_rate=0.2):
    weights = [0.0, 0.0]
    bias = 0.0

    for _ in range(epochs):
        for inputs, target in zip(samples, labels):
            prediction = step(sum(x * w for x, w in zip(inputs, weights)) + bias)
            error = target - prediction
            weights = [w + learning_rate * error * x for w, x in zip(weights, inputs)]
            bias += learning_rate * error

    return weights, bias


if __name__ == "__main__":
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    outputs = [0, 0, 0, 1]
    weights, bias = train_perceptron(inputs, outputs)

    print("Learned weights:", [round(weight, 2) for weight in weights])
    print("Learned bias:", round(bias, 2))
    for sample in inputs:
        value = sum(x * w for x, w in zip(sample, weights)) + bias
        print(sample, "=>", step(value))
