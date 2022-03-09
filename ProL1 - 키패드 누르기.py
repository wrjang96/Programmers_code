def solution(numbers, hand):
    answer = ''
    typing = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    lefthand = '*'
    righthand = '#'
    for i in range(len(numbers)):
        if numbers[i] % 3 == 1:
            answer += "L"
            lefthand = numbers[i]
        elif numbers[i] % 3 == 0 and numbers[i] !=0:
            answer += "R"
            righthand = numbers[i]
        else:
            tmpx=0; tmpy = 0
            lx = 0; ly=0; rx =0; ry= 0
            for k in range(4):
                for j in range(3):
                    if typing[k][j] == numbers[i]:
                        tmpx = k; tmpy = j
                    if typing[k][j] == lefthand:
                        lx = k; ly = j
                    if typing[k][j] == righthand:
                        rx = k; ry = j
            if abs(tmpx-lx) + abs(tmpy - ly) > abs(tmpx-rx) + abs(tmpy - ry):
                answer += "R"
                righthand = numbers[i]
                #print('compare right')
            elif abs(tmpx-lx) + abs(tmpy - ly) < abs(tmpx-rx) + abs(tmpy - ry):
                answer += "L"
                lefthand = numbers[i]
                #print('compare left')
            else:
                if hand == "left":
                    #print('hand left')
                    lefthand = numbers[i]
                    answer += "L"
                else:
                    #print('hand right')
                    righthand = numbers[i]
                    answer += "R"
    return answer