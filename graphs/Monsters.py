import sys, math, bisect
from collections import defaultdict, deque
input = sys.stdin.readline
 
sin, mulin, intin, arrin = lambda: input().strip(), lambda: map(int,input().split()), lambda: int(input()), lambda: list(map(int,input().split()))

def solve():
    n, m = mulin()
    grid = [sin() for _ in range(n)]

    st_x, st_y = -1, -1
    player = deque([])
    monsters = deque([])
    pehlaMonster = [[float('inf')] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                player.append((i, j))
                st_x, st_y = i, j
            elif grid[i][j] == 'M':
                monsters.append((i, j))
                pehlaMonster[i][j] = 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while monsters:
        for _ in range(len(monsters)):
            x, y = monsters.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m or pehlaMonster[nx][ny] <= pehlaMonster[x][y] + 1 or grid[nx][ny] == '#':
                    continue
                pehlaMonster[nx][ny] = pehlaMonster[x][y] + 1
                monsters.append((nx, ny))

    # for i in pehlaMonster:
    #     print(*i)

    par = [[-1] * m for _ in range(n)]
    par[st_x][st_y] = (st_x, st_y)
    steps = 0
    flag = False

    while player:
        for _ in range(len(player)):
            x, y = player.popleft()
            if pehlaMonster[x][y] <= steps:
                continue
            if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                path = []
                moves = {(0, 1): 'R', (1, 0): 'D', (-1, 0): 'U', (0, -1): 'L'}

                while (x, y) != (st_x, st_y):
                    px, py = par[x][y]
                    path.append(moves[(x - px, y - py)])
                    x, y = px, py

                print("YES")
                print(len(path))
                print(''.join(reversed(path)))
                sys.exit()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m or par[nx][ny] != -1 or grid[nx][ny] == '#' or steps + 1 >= pehlaMonster[nx][ny]:
                    continue
                par[nx][ny] = (x, y)
                player.append((nx, ny))
        steps += 1

    # for i in par:
    #     print(*i)

    if not flag:
        print("NO")

    
# for _ in range(intin()):
solve()