def get_bit(num, i):
    return (num >> i) & 1

def is_bit_set(num, i):
    return (num & (1 << i)) != 0

def set_bit(num, i):
    num = num | (1 << i)
    return num

def clear_bit(num, i):
    num = num & ~(1 << i)
    return num

def clear_most_significant_bits(num, i):
    num = num & ((1 << i) - 1)
    return num

def clear_least_significant_bits(num, i):
    num = num & ~((1 << (i + 1)) - 1)
    return num

def print_binary(num):
    s = ""
    for i in xrange(32, -1, -1):
        s += str(get_bit(num, i))
    print s


def main():
    SIZE = 33
    test_num = 2**33 - 1
    print_binary(test_num)

    print "\nget_bit"
    for pos in xrange(SIZE - 1, -1, -1):
        print "%s" % get_bit(test_num, pos),

    print "\nis_bit_set"
    for pos in xrange(SIZE - 1, -1, -1):
        print "%s " % is_bit_set(test_num, pos),

    print "\nset_bit"
    for pos in xrange(SIZE):
        print_binary(set_bit(test_num, pos))

    print "\nclear_bit"
    for pos in xrange(SIZE):
        print_binary(clear_bit(test_num, pos))

    print "\nclear_most_significant_bits"
    for pos in xrange(SIZE):
        print_binary(clear_most_significant_bits(test_num, pos))

    print "\nclear_least_significant_bits"
    for pos in xrange(SIZE):
        print_binary(clear_least_significant_bits(test_num, pos))


if __name__ == "__main__":
    main()
