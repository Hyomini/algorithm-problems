import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")

delta = [(0,0), (-1, 0), (0, 1), (1, 0), (0, -1)]
board_len = 10

def init_board(bc_info):
    for i in range(board_len):
        for j in range(board_len):
            for bc in range(A):
                bc_pos = (bc_info[bc][0], bc_info[bc][1])
                bc_cov = bc_info[bc][2]
                bc_perf = bc_info[bc][3]
                if abs(j - bc_pos[0]) + abs(i - bc_pos[1]) <= bc_cov:
                    if board[i][j] == 0:
                        board[i][j] = list()
                    board[i][j].append(bc_perf)
                    board[i][j].sort(reverse=True)

def solve():
    max_charge = 0
    a_pos = a_start
    b_pos = b_start
    for i in range(M):
        a_pos = (a_pos[0] + delta[a_move[i]][0], a_pos[1] + delta[a_move[i]][1])
        b_pos = (b_pos[0] + delta[b_move[i]][0], b_pos[1] + delta[b_move[i]][1])
        if a_pos == b_pos and board[a_pos[0]][a_pos[1]] != 0:
            if len(board[a_pos[0]][a_pos[1]]) > 1:
                max_charge += max(max(board[a_pos[0]][a_pos[1]]), board[a_pos[0]][a_pos[1]][0] + board[a_pos[0]][a_pos[1]][1])
            else:
                max_charge += board[a_pos[0]][a_pos[1]][0]
        else:
            if board[a_pos[0]][a_pos[1]] != 0:
                max_charge += max(board[a_pos[0]][a_pos[1]])
            if board[b_pos[0]][b_pos[1]] != 0:
                max_charge += max(board[b_pos[0]][b_pos[1]])

    return max_charge


T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))

    bc_info = defaultdict(list)
    for i in range(A):
        bc_info[i].extend(list(map(int, input().split())))
        bc_info[i][0] -= 1
        bc_info[i][1] -= 1

    board = [[0] * board_len for _ in range(board_len)]
    a_start = (0, 0)
    b_start = (9, 9)
    init_board(bc_info)
    ans = 0
    ans = solve()

    print(f'#{test_case} {ans}')