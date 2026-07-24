import sys, math, bisect, heapq
from collections import defaultdict
input = sys.stdin.readline
 
sin, mulin, intin, arrin = lambda: input().strip(), lambda: map(int,input().split()), lambda: int(input()), lambda: list(map(int,input().split()))

def solve():
    n, m = mulin()
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = mulin()
        adj[a].append((b, c))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    heap = [(0, 1)]

    while heap:
        d, u = heapq.heappop(heap)

        if d != dist[u]:
            continue

        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))

    print(*dist[1:]) 
    
# for _ in range(intin()):
solve()