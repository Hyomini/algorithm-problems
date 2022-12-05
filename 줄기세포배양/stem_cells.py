import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
delta = [(0,1),(1,0),(-1,0),(0,-1)]

def init_grid():
    grid_xlen = N + 2*K
    grid_ylen = M + 2*K
    grid = [[0] * grid_ylen for _ in range(grid_xlen)]

    for i in range(N):
        for j in range(M):
            grid[K + i][K + j] = origin_cells[i][j]

    return grid

# key: position, value[0]: 생명력, value[1]: 수명
def update_grid():
    # active cells 업데이트
    # 1. 수명이 0보다 큰 cell의 수명을 1씩 감소시킨다
    # 2. 수명이 0인 cell을 remove
    active_keys = list(active_cells.keys())
    for cell_pos in active_keys:
        if active_cells[cell_pos][1] > 0:
            active_cells[cell_pos][1] -= 1
    for cell_pos in active_keys:
        if active_cells[cell_pos][1] == 0:
            active_cells.pop(cell_pos)
            grid[cell_pos[0]][cell_pos[1]] = -1

    # 1. 번식(inactive cells에서 수명이 0이면 사방에 번식, max값으로 갱신)
    # 1-2. 수명이 0인 cell을 inactive cells에서 remove
    # 1-3. 수명이 0보다 큰 cell의 수명을 1씩 감소시킨다
    inactive_keys = list(inactive_cells.keys())
    reproduce_targets = list()
    for cell_pos in inactive_keys:
        if inactive_cells[cell_pos][1] == 0:
            reproduce_targets.append(cell_pos)
        if inactive_cells[cell_pos][1] > 0:
            inactive_cells[cell_pos][1] -= 1
    # reproduce
    for target in reproduce_targets:
        reproduce(target)
        inactive_cells.pop(target)

    # 수명이 0인 cell들 active cells에 추가
    inactive_keys = list(inactive_cells.keys())
    for cell_pos in inactive_keys:
        if inactive_cells[cell_pos][1] == 0:
            active_cells[cell_pos] = [inactive_cells[cell_pos][0], inactive_cells[cell_pos][0]]


def reproduce(cell_pos):
    for i in range(len(delta)):
        new_cellx, new_celly = cell_pos[0] + delta[i][0], cell_pos[1] + delta[i][1]
        if grid[new_cellx][new_celly] == 0 or (grid[new_cellx][new_celly] > 0 and inactive_cells[cell_pos][0] == inactive_cells[cell_pos][1]):
            grid[new_cellx][new_celly] = max(grid[new_cellx][new_celly], inactive_cells[cell_pos][0])
            inactive_cells[(new_cellx, new_celly)] = [grid[new_cellx][new_celly], grid[new_cellx][new_celly]]


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    active_cells = defaultdict(list)
    inactive_cells = defaultdict(list)
    origin_cells = [list(map(int, input().split())) for _ in range(N)]
    grid = init_grid()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                inactive_cells[(i,j)] = [grid[i][j], grid[i][j]]
    
    for i in range(1, K+1):
        update_grid()
    
    cnt = len(active_cells) + len(inactive_cells)

    print(f"#{test_case} {cnt}")