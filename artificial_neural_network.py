import math


def sigmoid(value):
    return 1 / (1 + math.exp(-value))


def neuron(inputs, weights, bias):
    return sigmoid(sum(x * w for x, w in zip(inputs, weights)) + bias)


def forward(inputs):
    hidden_1 = neuron(inputs, [0.4, -0.2], 0.1)
    hidden_2 = neuron(inputs, [0.3, 0.8], -0.3)
    output = neuron([hidden_1, hidden_2], [0.7, 0.5], -0.2)
    return hidden_1, hidden_2, output


if __name__ == "__main__":
    sample = [1, 0]
    h1, h2, result = forward(sample)

    print("Input:", sample)
    print("Hidden layer:", [round(h1, 3), round(h2, 3)])
    print("Network output:", round(result, 3))
    print("Predicted class:", 1 if result >= 0.5 else 0)
