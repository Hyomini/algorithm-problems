# import sys
# sys.stdin = open("input.txt", "r")


def get_cases():
    cases = list()
    for i in range(1 << len(pos_info)):
        temp = str(format(i, 'b')).zfill(len(pos_info))
        cases.append(list(map(int, temp)))

    return cases


def cal_time(people_pos, stair_info):
    cnt = 0
    dist = list()
    stair_len = board[stair_info[0]][stair_info[1]]
    for person_pos in people_pos:
        dist.append(abs(pos_info[person_pos][0] - stair_info[0]) + abs(pos_info[person_pos][1] - stair_info[1]) + stair_len)
    # if len(people_pos) <= 3:
    #     for i in range(len(people_pos)):
    #         cnt = max(dist[i], cnt)
    #     return cnt + 1
    # else:
    q = list()
    wait_q = list()
    while dist != [-1] * len(dist):
        cnt += 1
        for i in q[:]:
            dist[i] -= 1
            if dist[i] == 0:
                q.remove(i)
                dist[i] = -1
        for i in wait_q[:]:
            if len(q) < 3:
                wait_q.remove(i)
                q.append(i)
        for i in range(len(dist)):
            if i not in q and i not in wait_q:
                if dist[i] > stair_len:
                    dist[i] -= 1
                    if dist[i] == stair_len:
                        if len(q) < 3:
                            dist[i] += 1
                            q.append(i)
                        else:
                            wait_q.append(i)
        # print(stair_len, cnt, dist, q, wait_q)
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    pos_info = list()
    stairs_info = list()

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                pos_info.append([i, j])
            elif board[i][j] > 1:
                stairs_info.append([i, j])
    cases = get_cases()

    ans = float('inf')
    for case in cases:
        stair_a = [idx for idx, x in enumerate(case) if x == 0]
        stair_b = [idx for idx, x in enumerate(case) if x == 1]
        ans = min(ans, max(cal_time(stair_a, stairs_info[0]), cal_time(stair_b, stairs_info[1])))

    print(f"#{test_case} {ans}")