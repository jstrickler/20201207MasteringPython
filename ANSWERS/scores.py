#!/usr/bin/env python

sum_of_scores = 0.0

# biz logic
with open("../DATA/testscores.dat") as scores_in:

    for number_of_scores, line in enumerate(scores_in):
        (name, score) = line.split(":")
        score = int(score)
        sum_of_scores += score

        if score > 94:
            grade = 'A'
        elif score > 88:
            grade = 'B'
        elif score > 82:
            grade = 'C'
        elif score > 74:
            grade = 'D'
        else:
            grade = 'F'

        print("{:20s} {} {}".format(name, score, grade))

average = sum_of_scores/number_of_scores
print("\naverage score is  {:.2f}\n".format(average))
