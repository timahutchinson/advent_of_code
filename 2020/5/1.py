import numpy as np

with open("input.txt", "r") as f:
    lines = [val.strip() for val in f.readlines()]

def find_seat(inst, nrows):
    rows = np.arange(nrows)
    for i in inst:
        if (i == "F") or (i == "L"):
            rows = rows[:int(len(rows)/2)]
        elif (i == "B") or (i == "R"):
            rows = rows[int(len(rows)/2):]
    return rows[0]


def seat_id(seat):
    return find_seat(seat[:7], 128) * 8 + find_seat(seat[7:], 8)

maxi = 0
for seat in lines:
    this_seat_id = seat_id(seat)
    if this_seat_id > maxi:
        maxi = this_seat_id

print(maxi)
