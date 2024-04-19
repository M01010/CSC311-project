import os.path
import random
import string

from constants import TEXT_PATH, START, END, STEP, GENERATION_SEED


def get_random_char():
    # TODO: we can change how this works later to get different results
    return random.choice(string.ascii_letters)


def generate_files(start, end, step, seed=None):
    # use seed so everytime we generate the text we get the same output
    random.seed(seed)

    if not os.path.exists(TEXT_PATH):
        os.makedirs(TEXT_PATH)

    # for all i (100, 200, 300, ....., 10000)
    for i in range(start, end, step):
        filename = f'{TEXT_PATH}/{i}.txt'
        with open(filename, 'w') as f:
            # write i random characters
            for _ in range(i):
                # get random ascii character and write it
                c = get_random_char()
                f.write(c)


if __name__ == '__main__':
    generate_files(START, END, STEP, GENERATION_SEED)
