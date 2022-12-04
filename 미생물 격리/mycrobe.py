# import sys
#
# sys.stdin = open("input.txt", "r")

delta = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]


def cal_microbe_pos(hive):
    dir = delta[hive[3]]
    hive[0] = hive[0] + dir[0]
    hive[1] = hive[1] + dir[1]

    if hive[0] <= 0 or hive[0] >= N - 1 or hive[1] <= 0  or hive[1] >= N - 1:
        hive[2] = hive[2] // 2
        if hive[3] == 1:
            hive[3] = 2
        elif hive[3] == 2:
            hive[3] = 1
        elif hive[3] == 3:
            hive[3] = 4
        elif hive[3] == 4:
            hive[3] = 3


def rearrange():
    # 변화된 위치를 바탕으로 board 재계산
    board = [[[None]] * N for _ in range(N)]
    for idx, hive in enumerate(hive_info):
        hive_posx, hive_posy = hive[0], hive[1]
        if board[hive_posx][hive_posy] == [None]:
            board[hive_posx][hive_posy] = [idx]
        else:
            board[hive_posx][hive_posy].append(idx)

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                # hive_info를 조사해서 같은 위치를 가지는 군집들 확인
                # 가장 큰 미생물 수를 가진 군집에 미생물 몰아주고, 나머지 군집은 미생물 수 0 처리
                biggest_idx = max(board[i][j], key = lambda n: hive_info[n][2])
                for idx in board[i][j][:]:
                    if idx != biggest_idx:
                        hive_info[biggest_idx][2] += hive_info[idx][2]
                        hive_info[idx][2] = 0
                        board[i][j].remove(idx)


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    hive_info = [list(map(int, input().split())) for _ in range(K)]

    while M:
        M -= 1
        for hive in hive_info:
            if hive[2] > 0:
                cal_microbe_pos(hive)
        rearrange()

    ans = 0
    for hive in hive_info:
        ans += hive[2]
    print(f"#{test_case} {ans}")
