import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 활주로 건설 가능성을 체크
def is_possible(line):
    return True

for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        ans += 1 and is_possible(board[i])
        ans += 1 and is_possible([board[j][i] for j in range(N)])

    print(f'#{test_case} {ans}')