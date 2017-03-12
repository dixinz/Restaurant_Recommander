# This function returns the index of the recomended restaurant for a given
# person based on similarities between pairs of people and the restaurant
# ratings given by people.
# Author: Dixin Zhang
# Student ID: 804604
# Date created: 24th September
# Date modified: 5th October


def recommendation(person, ratings, similarities):
    # return -1 if the given person has no unrated restaurants
    if 0 not in ratings[person]:
        return -1

    # record the index of the given person's non-zero ratings
    index_nonzero_rating = []
    for i in range(len(ratings[person])):
        if ratings[person][i]:
            index_nonzero_rating.append(i)

    # lst_ratings records others' rating of each restaurant
    lst_ratings = list(ratings)
    lst_ratings.remove(lst_ratings[person])

    # ensure at least one other person has rated the restaurant which is rated
    # by the given person or return -1
    count = False
    for j in lst_ratings:
        if count:
            break
        for i in index_nonzero_rating:
            if j[i]:
                count = True
                break
    if not count:
        return -1

    # proceed to retrieve the index of the recommended restaurant
    if count:

        # record the index of the given person's non-zero rating
        index_zero_rating = sorted(set(range(len(ratings[person]))) -
                                   set(index_nonzero_rating))
        similarities = list(similarities)
        similarities.remove(similarities[person])

        # calculate each restaurant's weighted average ratings given by others
        # who has rated it and record the index of that restaurant
        score_index = []
        for i in index_zero_rating:
            numerator = denominator = 0
            for j in range(len(similarities)):
                numerator += similarities[j][person]*ratings[j][i]
                denominator += similarities[j][person]
            score = numerator/denominator
            score_index.append((score, i))

        # return the highest weighted average rated restaurant's index
        return max(sorted(score_index, reverse=True))[1]
