import sys

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent, size):
    ra, rb = find(a, parent), find(b, parent)
    if ra == rb:
        return size[ra]
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return size[ra]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    parent = {}
    size   = {}
    for _ in range(N):
        u, v = sys.stdin.readline().split()
        for name in (u, v):
            if name not in parent:
                parent[name] = name
                size[name] = 1
        print(union(u, v, parent, size))
