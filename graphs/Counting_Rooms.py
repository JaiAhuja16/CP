import sys, math, bisect
from collections import defaultdict, deque
input = sys.stdin.readline
 
sin, mulin, intin, arrin = lambda: input().strip(), lambda: map(int,input().split()), lambda: int(input()), lambda: list(map(int,input().split()))

def solve():
    n, m = mulin()
    grid = [list(sin()) for _ in range(n)]

    rooms = 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    
    def bfs(x: int, y: int) -> None:
        q = deque([(x, y)])
        grid[x][y] = '#'
        while q:
            ux, uy = q.popleft()
            for dx, dy in dirs:
                nx, ny = ux + dx, uy + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[nx][ny] == '#':
                    continue
                q.append((nx, ny))
                grid[nx][ny] = '#'

    for x in range(n):
        for y in range(m):
            if grid[x][y] == '.':
                bfs(x, y)
                rooms += 1
    # print(grid)
    print(rooms)

# for _ in range(intin()):
solve()