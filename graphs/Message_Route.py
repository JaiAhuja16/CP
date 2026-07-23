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


    par = [-1] * (n + 1)

    q = deque([1])
    par[1] = 1
    c = 1

    while q:
        for _ in range(len(q)):
            u = q.popleft()
            if u == n:
                break
            for v in adj[u]:
                if par[v] == -1:
                    q.append(v)
                    par[v] = u
        c += 1
        if par[n] != -1:
            break

    if par[n] == -1:
        print("IMPOSSIBLE")
    else:
        print(c)
        path = []
        curr = n
        while curr != 1:
            path.append(curr)
            curr = par[curr]
        path.append(1)
        print(*reversed(path))
        
# for _ in range(intin()):
solve()