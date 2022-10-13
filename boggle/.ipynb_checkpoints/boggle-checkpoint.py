from collections import defaultdict

def isAround(prev_pos, rest_word):
    if len(rest_word) == 1:
        return True
    
    next_char = rest_word[0]
    
    if next_char not in board.keys():
        return False

    # 인접한 위치인지 비교(x축, y축)
    for pos in board[next_char]:
        if pos == prev_pos:
            continue
        if pos[0] >= prev_pos[0] - 1 and pos[0] <= prev_pos[0] + 1 \
        and pos[1] >= prev_pos[1] - 1 and pos[1] <= prev_pos[1] + 1:
            return isAround(pos, rest_word[1:])

def isThere(word):
    if word[0] not in board.keys():
        return False
    
    if len(word) == 1:
        return True
    
    for position in board[word[0]]: 
        if isAround(position, word[1:]):
            return True
    return False

if __name__ == "__main__":
    # input 처리
    board_size = 5
    case_num = int(input())
    for _ in range(case_num):
        board = defaultdict(list)
        for x in range(board_size):
            for y, str in enumerate([*input()]):
                board[str].append((x, y))
        ans_num = int(input())
        answers = list()
        for i in range(ans_num):
            answers.append(input())
        
        # 답안 출력
        for answer in answers:
            if isThere(answer):
                result = 'YES'
            else:
                result = 'NO'
            print(f'{answer} {result}')