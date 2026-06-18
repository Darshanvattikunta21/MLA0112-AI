class DecisionNode:
    def __init__(self, question=None, yes_branch=None, no_branch=None, result=None):
        self.question = question
        self.yes_branch = yes_branch
        self.no_branch = no_branch
        self.result = result

    def is_leaf(self):
        return self.result is not None


def classify(node, answers):
    while not node.is_leaf():
        answer = answers.get(node.question, False)
        node = node.yes_branch if answer else node.no_branch

    return node.result


if __name__ == "__main__":
    tree = DecisionNode(
        question="has_fever",
        yes_branch=DecisionNode(
            question="has_cough",
            yes_branch=DecisionNode(result="Possible flu"),
            no_branch=DecisionNode(result="Possible infection"),
        ),
        no_branch=DecisionNode(
            question="has_rash",
            yes_branch=DecisionNode(result="Possible allergy"),
            no_branch=DecisionNode(result="Likely healthy"),
        ),
    )

    patient_answers = {
        "has_fever": True,
        "has_cough": True,
        "has_rash": False,
    }

    print("Decision tree result:", classify(tree, patient_answers))
