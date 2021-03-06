import itertools

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


seat_ids = [seat_id(seat) for seat in lines]

p_seat_ids = list(range(1024))
missing_seats = []
for seat in p_seat_ids:
    if seat not in seat_ids:
        if seat+1 in seat_ids:
            if seat-1 in seat_ids:
                print(seat)
