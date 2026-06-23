from collections import defaultdict


def q_learning(episodes=20, alpha=0.5, gamma=0.8):
    rewards = {
        "A": {"B": 0, "C": 0},
        "B": {"D": 1},
        "C": {"D": 2},
        "D": {},
    }
    q = defaultdict(float)

    for _ in range(episodes):
        for state, actions in rewards.items():
            for action, reward in actions.items():
                next_state = action
                next_best = max([q[(next_state, a)] for a in rewards[next_state]] or [0])
                q[(state, action)] += alpha * (reward + gamma * next_best - q[(state, action)])

    return q


if __name__ == "__main__":
    table = q_learning()
    for key in sorted(table):
        print(f"Q{key} = {round(table[key], 3)}")
    print("Best first action from A: C")
