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
    def test_algorithms(algorithms, trials=20):
        results = []
        for n in range(START, END, STEP):
            filename = f'{TEXT_PATH}/{n}.txt'
            with open(filename, 'r') as f:
                text = f.read()
            for p_length in range(2, P_MAX_LENGTH):
                p_location, p = TestPerf.get_pattern(text, n, p_length)
                for _ in range(trials):
                    for alg in algorithms:
                        time_ns, res = TestPerf.calc_time(alg, text, p)
                        results.append((alg.__name__, n, p_length, time_ns))
                        # if res != p_location:
                            # for early finds
                            # print(f'error {alg.__name__} {res} {p_location} {n}')
        return results

    @staticmethod
    def write_output(results):
        with open('output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('algorithm', 'string_length', 'pattern_length', 'avg_time_ns'))
            writer.writerows(results)

    @staticmethod
    def calc_time(alg, text, p):
        start = time.perf_counter_ns()
        res = alg(text, p)
        end = time.perf_counter_ns()
        time_ns = end - start
        return time_ns, res
