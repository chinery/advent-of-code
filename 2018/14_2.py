# not too difficult to just check the last n entries to see if they match instead
# it just means having to keep generating numbers longer... my eagerness to
# pre-allocate the list in part 1 meant that this version basically re-implements the
# built-in list growing mechanism without the benefit of size(), append() etc.
# After doing some reading it seems trying to set an 'initial capacity' (as you would
# do in Java with new ArrayList<>(100000)) is not really worth it in terms of
# optimisation. I might try making a pure-list version to compare.
#
# ... sure enough, they both take about 25 secs, so see 14_2v2 for cleaner code.

if __name__ == "__main__":
    try:
        while True:
            line = input()
            target = [int(x) for x in list(line)]
    except EOFError:
        pass

    scores = [0] * 300000
    scores[0] = 3
    scores[1] = 7

    elf1 = 0
    elf2 = 1
    endptr = 2

    while True:
        while endptr < len(scores) - 1:
            combined = scores[elf1] + scores[elf2]
            if combined > 9:
                scores[endptr] = combined // 10
                endptr += 1

                if endptr > len(target):
                    recent = scores[endptr-len(target):endptr]
                    if recent == target:
                        print(endptr-len(target))
                        quit()

                scores[endptr] = combined % 10
                endptr += 1

                if endptr > len(target):
                    recent = scores[endptr - len(target):endptr]
                    if recent == target:
                        print(endptr - len(target))
                        quit()

            else:
                scores[endptr] = combined
                endptr += 1

                if endptr > len(target):
                    recent = scores[endptr-len(target):endptr]
                    if recent == target:
                        print(endptr-len(target))
                        quit()

            elf1 = (elf1 + scores[elf1] + 1) % endptr
            elf2 = (elf2 + scores[elf2] + 1) % endptr
        scores.extend([0] * len(scores))

