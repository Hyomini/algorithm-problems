import sys
from collections import deque
sys.stdin = open("input.txt", "r")

delta = deque([(1, 1), (1, -1), (-1, -1), (-1, 1)])


def dfs(pos):
    sides = [1, 0, 0, 0]
    stack = list()
    stack.append([pos, 0, sides[:], [area[pos[0]][pos[1]]]])
    cases = []
    while stack:
        cur_pos, order, cur_sides, visited  = stack.pop()
        for dir in delta:
            next_posx, next_posy = cur_pos[0] + dir[0], cur_pos[1] + dir[1]
            if next_posx >= 0 and next_posx < N and next_posy >= 0 and next_posy < N and \
                area[next_posx][next_posy] not in visited: # 1) area 안에 있어야 한다. 2) 같은 종류의 디저트며 안된다.
                if delta.index(dir) == order:
                    if order != 0 and order != 1 and sides[order % 2] == sides[order]:
                        if order == 3:
                            continue
                        elif order == 4:
                            cases.append(sum(visited))
                            continue
                    cur_sides[order] += 1
                elif order + 1 < 4 and delta.index(dir) == order + 1: # 가던길을 되돌아오면 안된다.
                    cur_sides[order + 1] += 1
                    order += 1
                visited.append(area[next_posx][next_posy])
                stack.append([(next_posx, next_posy), order, cur_sides[:], visited[:]])
    return cases


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            cases = dfs((i, j))
    if len(cases) == 0:
        ans = -1
    else:
        ans = max(cases)

    print(f"#{test_case} {ans}")