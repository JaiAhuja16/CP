import sys, math, bisect
from collections import defaultdict, deque
input = sys.stdin.readline
 
sin, mulin, intin, arrin = lambda: input().strip(), lambda: map(int,input().split()), lambda: int(input()), lambda: list(map(int,input().split()))

def solve():
    n, m = mulin()
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = mulin()
        adj[u].append(v)
        adj[v].append(u)

    components = []

    visited = [False] * (n + 1)

    for city in range(1, n + 1):
        if not visited[city]:
            components.append(city)
            q = deque([city])
            visited[city] = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True
    print(len(components) - 1)
    for i in range(len(components) - 1):
        print(components[i], components[i + 1])

# for _ in range(intin()):
solve()