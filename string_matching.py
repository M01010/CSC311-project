def bruteforce(text, p) -> int:
    m = len(p)
    n = len(text)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == p[j]:
            j += 1
        if j == m:
            return i
    return -1


NO_OF_CHARS = 256


def generate_shift_table(p):
    skip_list = {}
    for i in range(len(p)):
        skip_list[p[i]] = max(1, len(p) - i - 1)
    return skip_list


def boyer_moore(text, p):
    m = len(p)
    n = len(text)
    bad_chars = generate_shift_table(p)
    i = m - 1
    while i <= n - 1:
        j = 0
        while j < m and p[m - j - 1] == text[i - j]:
            j += 1
        if j == m:
            return i - m + 1
        else:
            shift = bad_chars.get(text[i + j], m)
            if shift == 0:
                shift = m - 1
            skips = shift - j

            if skips <= 0:
                i += 1
            else:
                i += skips
    return -1


def compute_prefix(pattern):
    m = len(pattern)
    prefix = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix[length - 1]
            else:
                prefix[i] = 0
                i += 1

    return prefix


def kmp(text, p):
    n = len(text)
    m = len(p)
    prefix = compute_prefix(p)

    i = j = 0
    while i < n:
        if p[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1

    return -1
