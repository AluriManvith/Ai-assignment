def moves(a, b, x, y):
    return [
        (x, b),
        (a, y),
        (0, b),
        (a, 0),
        (min(x, a + b), b - (min(x, a + b) - a)),
        (a - (min(y, a + b) - b), min(y, a + b))
    ]


# DFS
def dfs(x, y, target):
    stack = [(0, 0, [])]
    visited = set()

    while stack:
        a, b, path = stack.pop()

        if (a, b) in visited:
            continue

        path = path + [(a, b)]
        visited.add((a, b))

        if a == target or b == target:
            return path

        for na, nb in moves(a, b, x, y):
            if (na, nb) not in visited:
                stack.append((na, nb, path))


# Depth limited search
def dls(x, y, target, limit):
    stack = [(0, 0, [], 0)]
    visited = set()

    while stack:
        a, b, path, depth = stack.pop()

        if depth > limit:
            continue

        if (a, b) in visited:
            continue

        path = path + [(a, b)]
        visited.add((a, b))

        if a == target or b == target:
            return path

        for na, nb in moves(a, b, x, y):
            stack.append((na, nb, path, depth + 1))


# Iterative deepening DFS
def iddfs(x, y, target, max_depth):
    for depth in range(max_depth):
        result = dls(x, y, target, depth)
        if result:
            return result


x = 4
y = 3
target = 2

print(dfs(x, y, target))
print(dls(x, y, target, 10))
print(iddfs(x, y, target, 10))