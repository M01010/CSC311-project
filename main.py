from string_matching import bruteforce, kmp, boyer_moore
from test_perf import TestPerf


def main():
    results = TestPerf.test_algorithms([bruteforce])
    TestPerf.write_output(results)


if __name__ == '__main__':
    main()
