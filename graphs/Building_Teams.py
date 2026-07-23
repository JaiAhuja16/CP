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

    teams = [-1] * (n + 1)
    flag = True

    for node in range(1, n + 1):
        if teams[node] == -1:
            q = deque([node])
            teams[node] = 1

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if teams[v] == teams[u]:
                        flag = False
                        break
                    if teams[v] == -1:
                        teams[v] = 3 - teams[u]
                        q.append(v)
                if not flag:
                    break
        
    if not flag:
        print("IMPOSSIBLE")
    else:
        print(*teams[1:])

# for _ in range(intin()):
solve()