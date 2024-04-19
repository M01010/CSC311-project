import time
import csv

from constants import START, END, STEP, TEXT_PATH, P_MAX_LENGTH


class TestPerf:
    @staticmethod
    def get_pattern(text, i, p_length):
        # TODO: we can change how this works later to get different results
        mid = i // 2
        return mid, text[mid:mid + p_length + 1]

    @staticmethod
    def test_algorithms(algorithms, n=5):
        results = []
        for alg in algorithms:
            for i in range(START, END, STEP):
                filename = f'{TEXT_PATH}/{i}.txt'
                with open(filename, 'r') as f:
                    text = f.read()
                for p_length in range(2, P_MAX_LENGTH):
                    p_location, p = TestPerf.get_pattern(text, i, p_length)

                    start = time.perf_counter_ns()
                    for _ in range(n):
                        res = alg(text, p)
                        if res != p_location:
                            # for early finds
                            print(f'error {alg.__name__} {res} {p_location} {i}')
                    end = time.perf_counter_ns()
                    avg = (end - start) / n

                    results.append((alg.__name__, i, p_length, avg))
        return results

    @staticmethod
    def write_output(results):
        with open('output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('algorithm', 'string_length', 'pattern_length', 'avg_time_ns'))
            writer.writerows(results)
