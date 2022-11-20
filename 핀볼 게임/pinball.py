# import sys
from collections import deque
from collections import defaultdict

# sys.stdin = open("input.txt", "r")

delta = [(0,1), (0,-1), (1, 0), (-1, 0)] # 동서남북
change_dir = [
    [0, 1, 2, 3], # 0: 동쪽 -> 동쪽, 서쪽 -> 서쪽, 남쪽 -> 남쪽, 북쪽 -> 북쪽
    [1, 3, 0, 2], # 1: 동쪽 -> 서쪽, 서쪽 -> 북쪽, 남쪽 -> 동쪽, 북쪽 -> 남쪽
    [1, 2, 3, 0], # 2: 동쪽 -> 서쪽, 서쪽 -> 남쪽, 남쪽 -> 북쪽, 북쪽 -> 동쪽
    [2, 0, 3, 1], # 3: 동쪽 -> 남쪽, 서쪽 -> 동쪽, 남쪽 -> 북쪽, 북쪽 -> 서쪽
    [3, 0, 1, 2], # 4: 동쪽 -> 북쪽, 서쪽 -> 동쪽, 남쪽 -> 서쪽, 북쪽 -> 남쪽
    [1, 0, 3, 2]  # 5: 동쪽 -> 서쪽, 서쪽 -> 동쪽, 남쪽 -> 븍쪽, 북쪽 -> 남쪽
]


def solve(start_pos, dir):
    cnt = 0
    cur_x, cur_y = start_pos[0] + delta[dir][0], start_pos[1] + delta[dir][1]
    while board[cur_x][cur_y] != -1 and (cur_x, cur_y) != start_pos:
        block_num = board[cur_x][cur_y]
        if block_num < 6:
            dir = change_dir[block_num][dir]
            if block_num > 0:
                cnt += 1
        else: # 웜홀에 접촉
            warmhole_in = warmhole_info[block_num].index((cur_x, cur_y))
            warmhole_out = warmhole_info[block_num][(warmhole_in + 1) % 2]
            cur_x, cur_y = warmhole_out
        cur_x += delta[dir][0]
        cur_y += delta[dir][1]
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [[5] * (N+2)]
    for i in range(N):
        board.append([5] + list(map(int, input().split())) + [5])
    board.append([5] * (N+2))

    start_pos_list = deque()
    warmhole_info = defaultdict(list)
    for i in range(N + 2):
        for j in range(N + 2):
            if board[i][j] == 0:
                start_pos_list.append((i, j))
            if board[i][j] > 5:
                warmhole_info[board[i][j]].append((i, j))

    ans = -1
    for start_pos in start_pos_list:
        for k in range(len(delta)):
            ans = max(ans, solve(start_pos, k))
    print(f'#{test_case} {ans}')