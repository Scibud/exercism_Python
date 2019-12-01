def latest(scores):
    return (scores[-1])             # Returns last entry
    


def personal_best(scores):
    scores.sort(reverse=True)       # Sorts in reverse order (Decending)
    return(scores[0])


def personal_top_three(scores):
    scores.sort(reverse=True)
    return(scores[0:3])             # Slices the list
   
