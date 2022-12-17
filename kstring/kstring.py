# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    target_str = list(input())
    len_str = len(target_str)

    part_str = set()
    for k in range(1, len_str + 1): # 부분문자열 길이
        for i in range(len_str):
            part_str.add(''.join(target_str[i:i + k]))
    ans = sorted(list(part_str))

    if K > len(ans):
        print(f"#{test_case} none")
    else:
        print(f"#{test_case} {ans[K - 1]}")