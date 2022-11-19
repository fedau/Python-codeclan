def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    elif final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    else:
        return "Tie"

def get_results(final_scores):
    result = []
    for match in final_scores:
        result.append(get_result(match))

    return result






    # (You could try and use a list comprehension for this)

