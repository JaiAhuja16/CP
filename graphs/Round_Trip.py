import sys, math, bisect
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(1000005)
 
sin, mulin, intin, arrin = lambda: input().strip(), lambda: map(int,input().split()), lambda: int(input()), lambda: list(map(int,input().split()))

def solve():
    n, m = mulin()
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = mulin()
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node: int, par: int, path: list[int]):
        path.append(node)
        visited[node] = True
        for v in adj[node]:
            if v == par:
                continue
            if visited[v]:
                if len(path) > 2:
                    op = path[path.index(v):] + [v]
                    print(len(op))
                    print(*op)
                    sys.exit()
                return
            dfs(v, node, path)
        path.pop()
            

    visited: list[bool] = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1, [])

    print("IMPOSSIBLE")
            
        
# for _ in range(intin()):
solve()