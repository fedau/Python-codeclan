def latest(scores):
    return scores[-1]


def personal_best(scores):
    # sorted(scores)
    # return scores[0]
    scores.sort(reverse = True)
    return scores[0]

def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[0:3]

def list_high_low(scores):
    scores.sort(reverse = True)
    return scores

