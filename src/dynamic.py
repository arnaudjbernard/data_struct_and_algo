def longest_common_subsequence_brute_force(str1, str2):
    n = len(str1)
    subsequence_count = 1 << n
    best_len = 0
    best_sub = ""

    for i in xrange(subsequence_count - 1, 0, -1):
        subsequence = ""
        for bit_index in xrange(n):
            bit_mask = 1 << bit_index
            if i & bit_mask:
                subsequence += str1[bit_index]
        if len(subsequence) > best_len and is_subsequence(subsequence, str2):
            best_len = len(subsequence)
            best_sub = subsequence
    return best_sub


def is_subsequence(subsequence, str2):
    n = len(str2)
    str_index = 0
    for c in subsequence:
        while str_index < n:
            if str2[str_index] == c:
                break
            str_index += 1
        else:
            return False

        str_index += 1
    return True


def longest_common_sequence_dynamic(str1, str2):
    n = len(str1)
    m = len(str2)
    values = [[0 for _ in xrange(m+1)] for _ in xrange(n+1)]
    for i in xrange(n+1):
        values[i][0] = 0
    for j in xrange(m+1):
        values[0][j] = 0
    for i in xrange(1, n+1):
        for j in xrange(1, m+1):
            if str1[i-1] == str2[j-1]:
                values[i][j] = values[i-1][j-1] + 1
            else:
                values[i][j] = max(values[i-1][j], values[i][j-1])

    return _backtrack(str1, str2, values, n, m)


def _backtrack(str1, str2, values, i, j):
    if i == 0 or j == 0:
        return ""
    if str1[i-1] == str2[j-1]:
        return _backtrack(str1, str2, values, i-1, j-1) + str1[i-1]
    if values[i][j-1] > values[i-1][j]:
        return _backtrack(str1, str2, values, i, j-1)
    else:
        return _backtrack(str1, str2, values, i-1, j)


def main():
    import string
    import random
    import sys
    a_l = list(string.lowercase)
    b_l = list(string.lowercase)
    a = b = bf = dyn = ""
    loops = 0
    while len(bf) == len(dyn):
        loops += 1
        if loops > 10:
            break
        random.shuffle(a_l)
        random.shuffle(b_l)
        a = ''.join(a_l[:10])
        b = ''.join(b_l[:10])
        bf = longest_common_subsequence_brute_force(a, b)
        dyn = longest_common_sequence_dynamic(a, b)
        print a, b, bf, dyn
        sys.stdout.flush()
    else:
        print "error", a, b, bf, dyn


if __name__ == "__main__":
    main()
