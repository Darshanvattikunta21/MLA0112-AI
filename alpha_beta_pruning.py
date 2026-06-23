def alpha_beta(scores, depth, index, alpha, beta, maximizing):
    if depth == 0:
        return scores[index]

    if maximizing:
        best = float("-inf")
        for child in range(2):
            value = alpha_beta(scores, depth - 1, index * 2 + child, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    best = float("inf")
    for child in range(2):
        value = alpha_beta(scores, depth - 1, index * 2 + child, alpha, beta, True)
        best = min(best, value)
        beta = min(beta, best)
        if beta <= alpha:
            break
    return best


if __name__ == "__main__":
    terminal_scores = [3, 5, 6, 9, 1, 2, 0, -1]
    result = alpha_beta(terminal_scores, 3, 0, float("-inf"), float("inf"), True)
    print("Optimal value:", result)
