# import sys
from collections import defaultdict

# sys.stdin = open("input.txt", "r")

delta = [(0,0), (-1, 0), (0, 1), (1, 0), (0, -1)]
board_len = 10

def power(pos):
    bc_list = [0] * A
    for bc in range(A):
        if abs(bc_info[bc][1] - pos[0]) + abs(bc_info[bc][0] - pos[1]) <= bc_info[bc][2]:
            bc_list[bc] = bc_info[bc][3]
    return bc_list

def calculate(p1, p2):
    ret = 0

    if A == 1:
        return max(p1[0], p2[0])
    for i in range(A):
        for j in range(A):
            if i != j:
                ret = max(ret, p1[i] + p2[j])

    return ret

def solve():
    max_charge = 0
    a_pos = a_start
    b_pos = b_start
    for i in range(M):
        max_charge += calculate(power(a_pos), power(b_pos))
        a_pos = (a_pos[0] + delta[a_move[i]][0], a_pos[1] + delta[a_move[i]][1])
        b_pos = (b_pos[0] + delta[b_move[i]][0], b_pos[1] + delta[b_move[i]][1])
    
    max_charge += calculate(power(a_pos), power(b_pos))

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
    ans = 0
    ans = solve()

    print(f'#{test_case} {ans}')