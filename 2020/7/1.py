with open("input.txt", "r") as f:
    rules = [tuple(val.strip().split(" bags contain ")) for val in f.readlines()]

outer_bags = []
for rule in rules:
    if "shiny gold" in rule[1]:
        outer_bags.append(rule[0])

while True:
    nbags = len(outer_bags)
    for bag in outer_bags:
        for rule in rules:
            if (bag in rule[1]) and (rule[0] not in outer_bags):
                outer_bags.append(rule[0])
    if nbags == len(outer_bags):
        break

print(nbags)
