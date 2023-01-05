import sys
from collections import Counter

sys.stdin = open("input.txt", "r")


def get_square(posx, posy):
    lenx, leny = 0, 0
    # 사각형의 x, y축 길이 구하기
    for x in range(N - posx):
        if board[posx + x][posy] > 0:
            visited[posx + x][posy] = 1
            lenx += 1
        else:
            break
    for y in range(N - posy):
        if board[posx][posy + y] > 0:
            visited[posx][posy + y] = 1
            leny += 1
        else:
            break

    # 사각형 나머지 부분을 사각형으로 처리하기
    for i in range(lenx):
        for j in range(leny):
            visited[posx + i][posy + j] = 1

    return lenx, leny

def get_order(squares, cnt):
    orders = list()
    stack = list()
    for i in range(cnt):
        is_start = True
        target = squares[i][0]
        for j in range(cnt):
            if i != j and target in squares[j]:
                is_start = False
                break
        
        if is_start:
            orders.append(i)
            stack.append(squares[i][1])
            break
    
    while stack:
        num = stack.pop()
        for i in range(cnt):
            if i not in orders and squares[i][0] == num:
                orders.append(i)
                stack.append(squares[i][1])
    print(orders)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    squares = dict()

    square_cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j] > 0: # 사각형 시작점 찾기
                lenx, leny = get_square(i, j)
                squares[square_cnt] = [lenx, leny]
                square_cnt += 1
    get_order(squares, square_cnt)
    
    print(f"#{test_case} {squares}")