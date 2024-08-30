"This program will find out the max score from all the scores in a class."

scores = input("Enter all score: ").split()

for score in range(0, len(scores)):
    scores[score] = int(scores[score])

# print(scores)

highest_score = 0
for n in scores:
    if n > highest_score:
        highest_score = n

print(f"highest score: {highest_score}")
