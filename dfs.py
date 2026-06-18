def depth_first_search(graph, start):
    visited = set()
    order = []

    def visit(node):
        if node in visited:
            return

        visited.add(node)
        order.append(node)

        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return order


if __name__ == "__main__":
    sample_graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    print("DFS traversal:", depth_first_search(sample_graph, "A"))
