def runner_up(n, scores):

    if n == 2:
        if scores[0] == scores[1]:
            return scores[0]

    first = 0
    for i in range(n):
        if scores[i] >= first:
            first = scores[i]

    runner = 0
    for i in range(n):
        if scores[i] >= runner and scores[i] < first:
            runner = scores[i]

    return runner


print(runner_up(2,[2,2]))