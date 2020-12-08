from collections import Counter

print(sum([j for sublist in [[1 if i == len(answer) else 0 for i in dict(Counter("".join(answer))).values()] for answer in [val.split() for val in open("input.txt", "r").read().split("\n\n")]] for j in sublist]))
