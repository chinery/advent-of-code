if __name__ == "__main__":
    try:
        total = 0
        while True:
            line = int(input())
            total += line//3 - 2
    except EOFError:
        pass

    print(total)

