# This function returns the average rating of all non-zero ratings by all
# people to all restaurants in regards of a given cuisine.
# Author: Dixin Zhang
# Student ID: 804604
# Date created: 24th September
# Date modified: 4th October


def ave_rating(cuisine, restaurants, ratings):
    # record all valid ratings
    score = 0
    # record the number of valid ratings
    count = 0

    # check each restaurant and rating
    for i in range(len(restaurants)):
        for j in range(len(ratings)):

            # if the restaurant is of the required type and is rated,
            # increment score and count
            if cuisine in restaurants[i]:
                score += ratings[j][i]
                if ratings[j][i]:
                    count += 1

    # if rating exists, return average rating
    if count:
        return score/count
    else:
        return 0.0
