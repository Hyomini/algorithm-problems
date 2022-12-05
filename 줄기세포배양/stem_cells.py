# import sys
# import pprint
from collections import defaultdict

# sys.stdin = open("input.txt", "r")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def init(N, M, start_map):
    map_xlen = N + 2 * K + 1
    map_ylen = M + 2 * K + 1
    life_info = defaultdict(list)

    life_map = [[0] * map_xlen for _ in range(map_ylen)]
    active_map = [[0] * map_xlen for _ in range(map_ylen)]
    for i in range(N):
        for j in range(M):
            life_map[i + K + 1][j + K + 1] = start_map[i][j]
            active_map[i + K + 1][j + K + 1] = start_map[i][j] * 2
            if start_map[i][j] != 0:
                life_info[start_map[i][j]].append((i + K + 1, j + K + 1))
    return life_map, active_map, life_info


T = int(input())
for t in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    start_map = [list(map(int, input().split())) for _ in range(N)]
    life_map, active_map, life_info = init(N, M, start_map)
    while K:
        K -= 1
        tmp = sorted(list(life_info), reverse=True)
        for i in tmp:
            size = len(life_info[i])
            for j in range(size):
                x, y = life_info[i].pop(0)
                active_map[x][y] -= 1
                if active_map[x][y] < life_map[x][y]:
                    for k in range(4):
                        tx = x + dx[k]
                        ty = y + dy[k]
                        if life_map[tx][ty] == 0:
                            life_map[tx][ty] = i
                            active_map[tx][ty] = i * 2
                            life_info[i].append((tx, ty))
                if active_map[x][y] > 0:
                    life_info[i].append((x, y))
    count = 0
    for i in life_info:
        count += len(life_info[i])
    print(f"#{t} {count}")