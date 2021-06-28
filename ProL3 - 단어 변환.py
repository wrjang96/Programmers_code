queue = []
visited = ([])
def solution(begin, target, words):
    answer = 0
    queue.append([begin, 0])
    visited.append(begin)
    while queue:
        tmpstr, cnt = queue.pop(0)
        if tmpstr == target:
            answer = cnt
            break
        else:
            for i in range(len(begin)):
                tmp_begin = tmpstr[0:i] + tmpstr[i + 1: len(begin)]
                for j in range(len(words)):
                    tmp_words1 = words[j]
                    tmp_words2 = tmp_words1[0:i] + tmp_words1[i+1:len(begin)]
                    if tmp_begin == tmp_words2 and words[j] not in visited:
                        queue.append([words[j],cnt +1])
                        visited.append(words[j])
    return answer
#print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

