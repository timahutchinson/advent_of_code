from collections import Counter

with open("input.txt", "r") as f:
    answers = [val.split() for val in f.read().split("\n\n")]

count = 0
for answer in answers:
    anslen = len(answer)
    counts = dict(Counter("".join(answer)))
    for val in counts.values():
        if val == anslen:
            count += 1

print(count)
