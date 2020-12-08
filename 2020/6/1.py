print(sum([len(set(val)) for val in ["".join(i.split()) for i in open("input.txt", "r").read().split("\n\n")]]))


