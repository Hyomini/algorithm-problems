from collections import defaultdict, deque

# import sys
# sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    vertex = [x for x in range(1, V + 1)]
    edges = defaultdict(list)

    not_start = set()
    for i in range(0, len(temp), 2):
        edges[temp[i]].append(temp[i + 1])
        not_start.add(temp[i + 1])

    q = deque(set(vertex) - not_start)
    # print(f"edges: {edges}, start: {q}")
    ans = list()
    while len(ans) < V:
        cur_vtx = q.popleft()
        # print(q, cur_vtx, ans)
        if cur_vtx in ans:
            continue
        ans.append(cur_vtx)
        for edge in edges:
            if cur_vtx in edges[edge] and edge not in ans:
                ans.remove(cur_vtx)
                break
        if cur_vtx in ans:
            q.extend(edges[cur_vtx])
    
    print(f"#{test_case}", end=' ')
    for i in ans:
        print(i,end=' ')
    print()