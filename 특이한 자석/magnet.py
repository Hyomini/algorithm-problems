from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")

delta = [-1, 1]
score_info = [1, 2, 4, 8]
close_info = { # close_info[n][m]일 때, n번 자석에서 m번 자석과 맞닿는 날의 인덱스값, 0은 맞닿지 않는다는 의미
    0: [0,2,0,0],
    1: [6,0,2,0],
    2: [0,6,0,2],
    3: [0,0,6,0]
}
MAGNET_NUM = 4
MAGNET_LEN = 8
# N = 0, S = 1


def rotate(direction, magnet):
    if direction == 1: # 시계 방향
        magnet_temp = [magnet[-1]] + magnet[:MAGNET_LEN - 1]
        magnet = magnet_temp
    else: # direction == -1, 반시계 방향
        magnet_temp = magnet[1:] + [magnet[0]]
        magnet = magnet_temp
    return magnet


def rearrange(magnets, rotate_info):
    new_magnets = [None] * MAGNET_NUM
    visited = [False] * MAGNET_NUM
    q = deque()
    q.append(rotate_info)

    # BFS
    while q:
        idx, dir = q.popleft()
        new_magnets[idx] = rotate(dir, magnets[idx])
        for i in delta:
            next_idx = idx + i
            if 0 <= next_idx < MAGNET_NUM and not visited[next_idx]:
                if magnets[idx][close_info[idx][next_idx]] != magnets[next_idx][close_info[next_idx][idx]]:
                    q.append((next_idx, -dir)) # 반대방향을 큐에 삽입

        if not visited[idx]:
            visited[idx] = True

    # 회전되지 않은 자석을 원래 자석날순으로 assign
    for i in range(MAGNET_NUM):
        if new_magnets[i] is None:
            new_magnets[i] = magnets[i]

    return new_magnets


T = int(input())
for test_case in range(1, T + 1):
    score = 0
    K = int(input().strip())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    rotate_infos = [list(map(int, input().split())) for _ in range(K)]

    for rotate_info in rotate_infos:
        rotate_info[0] -= 1

    for i in range(K):
        magnets = rearrange(magnets=magnets, rotate_info=rotate_infos[i])

    for i in range(MAGNET_NUM):
        if magnets[i][0] == 1:
            score += score_info[i]

    print(f'#{test_case} {score}')