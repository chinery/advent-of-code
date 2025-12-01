def get_data():
    with open("1.txt") as file:
        data = [line.strip() for line in file.readlines()]

    data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    return data


data = get_data()

dial = 50
zeroes = 0

for line in data:
    val = int(line[1:])
    if line[0] == "L":
        val *= -1

    dial = (dial + val) % 100

    if dial == 0:
        zeroes += 1

print(zeroes)
