def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    database = {}
    for r in report:
        first, sec = r.split(" ")
        if sec not in database:
            database[sec] = [first]
        else:
            database[sec].append(first)
    for key, value in database.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1

    return answer