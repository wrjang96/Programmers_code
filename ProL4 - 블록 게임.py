def find_erasable_tetris(board, num):
    answer = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                answer.append([i, j])
    # print(answer)
    if len(answer) != 0 :
        # 오른 옆으로 긴 ㄴ
        if answer[1][0] == answer[0][0] + 1 and answer[1][1] == answer[0][1] and answer[2][0] == answer[0][0] + 1 and \
                answer[2][1] == answer[0][1] + 1 and answer[3][0] == answer[0][0] + 1 and answer[3][1] == answer[0][
            1] + 2:
            flag = True
            for i in range(answer[0][0] + 1):
                if board[i][answer[0][1] + 1] != 0:
                    flag = False
                    continue
                if board[i][answer[0][1] + 2] != 0:
                    flag = False
                    continue
            # print(flag)
            return flag

        # 왼쪽 옆으로 긴 ㄴ
        if answer[0][0] + 1 == answer[1][0] == answer[2][0] == answer[3][0] and answer[1][1] + 2 == answer[0][1] and answer[2][1] + 1 == answer[0][1] and answer[3][1] == answer[0][1]:
            flag = True
            for i in range(answer[0][0] + 1):
                if board[i][answer[0][1] - 1] != 0:
                    flag = False
                    continue
                if board[i][answer[0][1] - 2] != 0:
                    flag = False
                    continue
            # print(flag)
            return flag
        # ㅗ
        if answer[0][0] + 1 == answer[1][0] == answer[2][0] == answer[3][0] and answer[0][1] == answer[1][1] + 1 == answer[2][1] == answer[3][1] - 1:
            flag = True
            for i in range(answer[0][0] + 1):
                if board[i][answer[0][1] + 1] != 0:
                    flag = False
                    continue
                if board[i][answer[0][1] - 1] != 0:
                    flag = False
                    continue
            # print(flag)
            return flag
        # 오른쪽 긴 ㄴ
        if answer[0][0] + 1 == answer[1][0] == answer[2][0] - 1 == answer[3][0] - 1 and answer[0][1] == answer[1][1] == answer[2][1] == answer[3][1] - 1:
            flag = True
            for i in range(answer[0][0] + 2):
                if board[i][answer[0][1] + 1] != 0:
                    flag = False
                    continue
            # print(flag)
            return flag
        # 왼쪽 긴 ㄴ
        if answer[0][0] + 1 == answer[1][0] == answer[2][0] - 1 == answer[3][0] - 1 and answer[0][1] == answer[1][1] == answer[2][1] + 1 == answer[3][1]:
            flag = True
            for i in range(answer[0][0] + 2):
                if board[i][answer[0][1] - 1] != 0:
                    flag = False
                    continue
            # print(flag)
            return flag



def solution(board):
    answer = 0
    max_num = 0
    breakable_tetris = []
    for i in range(len(board)):
        max_num = max(max(board[i]), max_num)
        # 몇번까지 반복문 돌려야하나 알기 위함

    while 1:
        for i in range(1, max_num + 1):
            if find_erasable_tetris(board, i) == True:
                breakable_tetris.append(i)
        if len(breakable_tetris) == 0:
            break
        for num in breakable_tetris:
            answer += 1
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == num:
                        board[i][j] = 0
        breakable_tetris.clear()

    return answer

# print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
print(solution([[0, 1, 0], [0, 1, 0], [1, 1, 0]]))