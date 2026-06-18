def minimax(scores, depth, index, is_maximizing):
    if depth == 0:
        return scores[index]

    if is_maximizing:
        best_score = float("-inf")
        best_score = max(best_score, minimax(scores, depth - 1, index * 2, False))
        best_score = max(best_score, minimax(scores, depth - 1, index * 2 + 1, False))
        return best_score

    best_score = float("inf")
    best_score = min(best_score, minimax(scores, depth - 1, index * 2, True))
    best_score = min(best_score, minimax(scores, depth - 1, index * 2 + 1, True))
    return best_score


if __name__ == "__main__":
    terminal_scores = [3, 5, 2, 9, 12, 5, 23, 23]
    tree_depth = 3

    print("Best score:", minimax(terminal_scores, tree_depth, 0, True))
