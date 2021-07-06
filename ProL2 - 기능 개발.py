from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    time = deque([])
    answer = [1]
    for i in range(len(progresses)):
        tmp_percent = progresses.popleft()
        tmp_speed = speeds.popleft()
        if (100 - tmp_percent)%tmp_speed == 0:
            time.append((100 - tmp_percent)//tmp_speed)
        else:
            time.append(((100 - tmp_percent)//tmp_speed) + 1)
    time_flag = time[0]
    time_cnt = 0
    for i in range(1, len(time),1):
        if time_flag >= time[i]:
            answer[time_cnt] +=1
        else:
            answer.append(1)
            time_cnt +=1
            time_flag = time[i]
    return answer