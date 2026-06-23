def is_valid(region, color, assignment, neighbors):
    return all(assignment.get(neighbor) != color for neighbor in neighbors[region])


def color_map(regions, colors, neighbors, assignment=None):
    assignment = assignment or {}
    if len(assignment) == len(regions):
        return assignment

    region = next(item for item in regions if item not in assignment)
    for color in colors:
        if is_valid(region, color, assignment, neighbors):
            assignment[region] = color
            result = color_map(regions, colors, neighbors, assignment)
            if result:
                return result
            del assignment[region]

    return None


if __name__ == "__main__":
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    neighbors = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": [],
    }
    solution = color_map(regions, ["red", "green", "blue"], neighbors)

    print("Map coloring solution:")
    for region in regions:
        print(region, "=", solution[region])
