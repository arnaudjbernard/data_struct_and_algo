
def getSubsets(s):
    """
    :param s: set[int]
    :return: set[tuple[int]]
    """
    if not s:
        return frozenset([()])
    tot = set()
    e = s.pop()
    subsets = getSubsets(s)
    tot.update(subsets)
    for t in subsets:
        tot.update([(e,)+ t])

    return tot


def main():
    test_set = set(xrange(3))
    print getSubsets(test_set)


if __name__ == "__main__":
    main()
