from collections import deque
#defining the production rules
def moves(a, b, x, y):
    return [
        (x, b),
        (a, y),
        (0, b),
        (a, 0),
        (min(x, a + b), b - (min(x, a + b) - a)),
        (a - (min(y, a + b) - b), min(y, a + b))
    ]


# BFS
def bfs(x, y, target):
    visited = set()
    q = deque()
    q.append((0, 0, []))

    while q:
        a, b, path = q.popleft()

        if (a, b) in visited:
            continue

        path = path + [(a, b)]
        visited.add((a, b))

        if a == target or b == target:
            return path

        for na, nb in moves(a, b, x, y):
            if (na, nb) not in visited:
                q.append((na, nb, path))


# Bidirectional search
def bidirectional_bfs(x, y, target):
    start = {(0, 0)}
    end = {(target, 0), (0, target)}
    visited = set()

    while start and end:
        if start & end:
            return True

        new = set()
        for a, b in start:
            visited.add((a, b))
            for na, nb in moves(a, b, x, y):
                if (na, nb) not in visited:
                    new.add((na, nb))

        start = new
    return False


x = 4
y = 3
target = 2

print(bfs(x, y, target))
print(bidirectional_bfs(x, y, target))