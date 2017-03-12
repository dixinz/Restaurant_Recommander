# Author: Dixin Zhang
# Student ID: 804604
# Date created: 24th September
# Date modified: 4th October


from math import sqrt


def similarity(p1, p2, ratings):
    """
    This function returns the similarity between two people based on their
    respective tuple of restaurant ratings.
    """
    numerator = denominator_a = denominator_b = 0

    # check each person's rating of each restaurant and increment numerator
    # and denominator if rating is non-zero
    for (x, y) in zip(ratings[p1], ratings[p2]):
        if x and y:
            numerator += x*y
            denominator_a += x**2
            denominator_b += y**2

    # return 0.0 if denominator is 0
    if not denominator_a*denominator_b:
        return 0.0

    # otherwise return calculated similarity
    else:
        return numerator/(sqrt(denominator_a)*sqrt(denominator_b))
