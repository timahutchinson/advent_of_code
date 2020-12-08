import re

with open("testinput.txt", "r") as f:
    rules = [tuple(val.strip().split(" bags contain ")) for val in f.readlines()]

rules2 = []
for rule in rules:
    rules2.append((rule[0], [re.split("(?<=\d) ", val) for val in re.findall("(\d+ [\w ]+) bags?", rule[1])]))
    if rule[0] == "shiny gold":
        shiny_gold_holds = rules2[-1][1]
rules = dict(rules2)

for bag in shiny_gold_holds:
    nbags = int(bag[0])
    shiny_gold_holds += [[int(val[0]) * nbags, val[1]] for val in rules[bag[1]]]

print(sum([int(val[0]) for val in shiny_gold_holds]))
