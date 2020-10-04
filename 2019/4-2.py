def two_adj(x, banned=None):
    return len(x) > 1 and (
                (len(x) == 2 and x[0] == x[1] and x[0] != banned)
                or (len(x) > 2 and x[0] == x[1] and x[0] != x[2] and x[0] != banned)
                or (x[0] == x[1] and two_adj(x[1:], x[0]))
                or (x[0] != x[1] and two_adj(x[1:])))


def increasing(x):
    return len(x) == 1 or (x[0] <= x[1] and increasing(x[1:]))


possible = range(206938, 679128)
possible = map(str, possible)
possible = filter(two_adj, possible)
possible = filter(increasing, possible)

print(len(list(possible)))
