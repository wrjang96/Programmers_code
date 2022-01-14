import operator

def solution(genres, plays):
    answer = []
    database = {}
    temp = {}
    ranking = []
    for i in range(len(genres)):
        database[genres[i]] = database.get(genres[i],[]) + [(plays[i],i)]
        if genres[i] not in temp:
            temp[genres[i]] = plays[i]
        else:
            temp[genres[i]] = temp[genres[i]] + plays[i]
    temp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
    for i in temp:
         ranking.append(i[0])
    for i in ranking:
        tmp = sorted(database[i], key = lambda x:x[0] , reverse=True)
        for j in tmp[:2]:
            answer.append(j[1])
    print(database)
    return answer
