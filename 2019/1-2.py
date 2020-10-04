if __name__ == "__main__":
    try:
        total = 0
        while True:
            line = int(input())
            fuel = line//3 - 2
            while fuel > 0:
                total += fuel
                fuel = fuel//3 - 2
    except EOFError:
        pass

    print(total)

