def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    expected = []
    count = 0
    while(count < 3 and len(scores) > 0):
        maxval = max(scores)
        expected.append(maxval)
        scores.remove(maxval)
        count += 1
    return expected
