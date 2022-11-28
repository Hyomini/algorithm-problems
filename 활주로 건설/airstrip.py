# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

# 활주로 건설 가능성을 체크
def is_possible(line):
    if len(set(line)) == 1:
        return True

    check = False
    cnt = 1
    for i in range(1, N):
        if line[i-1] == line[i]:
            cnt += 1
        else:
            if check:
                if cnt < X:
                    return False
                check = False
                cnt -= X
            if line[i-1] - line[i] == 1:
                check = True
                cnt = 1
            elif line[i] - line[i-1] == 1: # line[i-1] < line[i]
                if cnt < X:
                    return False
                cnt = 1
            else:
                return False
    if check and cnt < X:
        return False
    return True

for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        ans += 1 and is_possible(board[i])
        ans += 1 and is_possible([board[j][i] for j in range(N)])

    print(f'#{test_case} {ans}')