
total = 0
try:
    line = input()
    while line is not None:
        if line[0] == '+':
            total += int(line[1:])
        elif line[0] == '-':
            total -= int(line[1:])
        line = input()
except EOFError:
    pass
    
print(total)
