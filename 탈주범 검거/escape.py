# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

delta = [[], [(0, 1), (0, -1), (1, 0), (-1, 0)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)],\
         [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [(R, C)]

    q = deque()
    q.append((R, C))
    while L - 1:
        L -= 1
        temp_q = set()
        while q:
            posx, posy = q.popleft()
            pipe = board[posx][posy]
            for dir in delta[pipe]:
                next_posx, next_posy = posx + dir[0], posy + dir[1]
                if next_posx >= 0 and next_posx < N and next_posy >= 0 and next_posy < M:
                    # 다음 위치의 파이프가 연결된 파이프인지 확인
                    is_connected = False
                    for dir2 in delta[board[next_posx][next_posy]]:
                        next_posx2, next_posy2 = next_posx + dir2[0], next_posy + dir2[1]
                        if next_posx2 == posx and next_posy2 == posy:
                            is_connected = True

                    if is_connected and board[next_posx][next_posy] > 0 and (next_posx, next_posy) not in visited:
                        temp_q.add((next_posx, next_posy))
                        visited.append((next_posx, next_posy))
        q.extend(temp_q)

    print(f"#{test_case} {len(visited)}")