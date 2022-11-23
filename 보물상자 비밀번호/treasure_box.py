# import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# sys.stdin = open("input.txt", "r")
T = int(input())


def get_numbers(number_length, number, window):
    numbers = list()
    for i in range(number_length):
        if i + window > number_length - 1:
            numbers.append(number[i:] + number[0:window - (number_length - 1 - i) - 1])
        else:
            numbers.append(number[i:i + window])

    numbers = sorted(list(set(numbers)), reverse=True)
    return numbers

def hex_to_decimal(num, window):
    hex_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    transformed_num = 0
    for i in range(len(num)):
        transformed_num += hex_map.index(num[i]) * (16 ** (window - i - 1))
    return transformed_num

for test_case in range(1, T + 1):
    N, K = map(int, sys.stdin.readline().split())
    number = sys.stdin.readline().split()[0]
    window = N // 4
    numbers = get_numbers(N, number, window)
    ans = numbers[K - 1]
    print(f'#{test_case} {hex_to_decimal(ans, window)}')