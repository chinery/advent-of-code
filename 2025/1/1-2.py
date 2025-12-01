def get_data():
    with open("1.txt") as file:
        data = [line.strip() for line in file.readlines()]

    data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L600",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    return data


data = get_data()

dial = 50
clicks = 0

for line in data:
    val = int(line[1:])
    start = dial

    if val > 100:
        clicks += val // 100
        val = val % 100

    if line[0] == "L":
        val *= -1

    dial += val

    if (dial <= 0 or dial >= 100) and (start != 0):
        clicks += 1

    dial = dial % 100
    print(line, start, dial, clicks)

print(clicks)
