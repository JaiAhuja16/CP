import sys, math, bisect
from collections import defaultdict, deque
input = sys.stdin.readline
 
# sys.setrecursionlimit(10000005)

sin, mulin, intin, arrin = lambda: input().strip(), lambda: map(int,input().split()), lambda: int(input()), lambda: list(map(int,input().split()))

def solve():
    n, m = mulin()
    grid = [sin() for _ in range(n)]

    st_x, st_y = -1, -1
    dest_x, dest_y = -1, -1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                st_x, st_y = i, j
            elif grid[i][j] == 'B':
                dest_x, dest_y = i, j

    if st_x == dest_x and st_y == dest_y:
        print("YES")
        print(0)
        print('')
        return

    path = []
    moves = {(0, 1): 'R', (1, 0): 'D', (-1, 0): 'U', (0, -1): 'L'}

    # def backtrack(curr_x, curr_y) -> str:
    #     if curr_x == st_x and curr_y == st_y:
    #         return
    #     diff = (curr_x - par[curr_x][curr_y][0], curr_y - par[curr_x][curr_y][1])
    #     path.append(moves[diff])
    #     # print(path)
    #     backtrack(par[curr_x][curr_y][0], par[curr_x][curr_y][1])

    q = deque([(st_x, st_y)])

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    par = [[-1] * m for _ in range(n)]

    par[st_x][st_y] = (st_x, st_y)

    while q:
        x, y = q.popleft()
        if x == dest_x and y == dest_y:
            x, y = dest_x, dest_y
            while (x, y) != (st_x, st_y):
                px, py = par[x][y]
                path.append(moves[(x - px, y - py)])
                x, y = px, py
            break
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or par[nx][ny] != -1 or grid[nx][ny] == '#':
                continue
            par[nx][ny] = (x, y)
            q.append((nx, ny))
        
    if not path:
        print("NO")
    else:
        print("YES")
        print(len(path))
        print(''.join(reversed(path)))

# for _ in range(intin()):
solve()