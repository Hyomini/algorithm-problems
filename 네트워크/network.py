# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")


def get_distance():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


T = int(input())
for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    N = temp[0]
    temp = temp[1:]
    dist = [[0] * N for _ in range(N)]

    for i in range(0, len(temp), N):
        dist[i//N] = (temp[i:i + N])
    for i in range(N):
        for j in range(N):
            if dist[i][j] == 0 and i != j:
                dist[i][j] = float('INF')

    get_distance()

    ans = 1000000

    for i in range(N):
        sum_dist = sum(dist[i])
        ans = min(ans, sum_dist)
    print(f"#{test_case} {ans}")