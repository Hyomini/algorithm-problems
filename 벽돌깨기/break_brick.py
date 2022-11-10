import sys
import itertools
import copy
from collections import deque

sys.stdin = open("input.txt", "r")
delta = [(0,-1), (0,1), (1,0), (-1,0)]

def get_permutations(N, W):
    return itertools.permutations(range(W), N)

def bomb(board, y_order, W, H):
    brick_num = 0
    for posy in y_order:
        q = deque()
        for posx in range(H):
            if board[posx][posy] > 0:
                board[posx][posy] = 0
                q.append((posx, posy))
                break
        while q:
            cur_x, cur_y = q.popleft()
            for i in range(len(delta)):
                for num in range(1, board[cur_x][cur_y]):
                    if board[cur_x + num * delta[i][0]][cur_y + num * delta[i][1]] > 1:
                        q.append((cur_x + num * delta[i][0], cur_y + num * delta[i][1]))
                    board[cur_x + num * delta[i][0]][cur_y + num * delta[i][1]] = 0
        sort_board(board, W, H)

    for i in range(H):
        for j in range(W):
            if board[i][j] > 0:
                brick_num += 1
    return brick_num

def sort_board(board, W, H):
    for j in range(W):
        for i in range(H - 1, -1, -1):
            if board[i][j] == 0:
                for k in range(i, -1, -1):
                    if board[k][j] > 0:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        break


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, W, H = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    brick_num = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] > 0:
                brick_num += 1

    y_orders = get_permutations(N, W)
    min_broken_brick_num = 181
    for y_order in y_orders:
        min_broken_brick_num = min(min_broken_brick_num, bomb(copy.deepcopy(board), y_order, W, H))
    print(f'#{test_case} {min_broken_brick_num}')