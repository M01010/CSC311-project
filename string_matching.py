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


def boyer_moore(text, p) -> int:
    pass


def kmp(text, p) -> int:
    pass
