#!/usr/env/bin python3

import os
import random

from attributedict.collections import AttributeDict
from tqdm import tqdm


def load(filename):
    streets = {}
    bs = []
    es = []
    ls = []
    paths = []
    with open(filename) as f:
        D, I, S, V, F = map(int, f.readline().split())
        in_streets = [[] for i in range(I)]
        out_streets = [[] for i in range(I)]
        for i in range(S):
            B, E, name, L = f.readline().split()
            B = int(B)
            E = int(E)
            L = int(L)
            streets[name] = (B, E, L)
            bs.append(B)
            es.append(E)
            ls.append(L)
            in_streets[E].append(name)
            out_streets[B].append(name)
        for i in range(V):
            l = f.readline().split()
            P = int(l[0])
            names = l[1:]
            paths.append(names)
    return AttributeDict({
        'D': D,
        'I': I,
        'S': S,
        'V': V,
        'F': F,
        'streets': streets,
        'in_streets': in_streets,
        'out_streets': out_streets,
        'bs': bs,
        'es': es,
        'ls': ls,
        'paths': paths
    })


def save(schedule, f):
    f.write(f'{len(schedule)}\n')
    for i, streets in enumerate(schedule):
        f.write(f'{i}\n')
        f.write(f'{len(streets)}\n')
        for name, t in streets:
            f.write(f'{name} {t}\n')


def score(data_set, schedule):
    # TODO: Implement
    return 0


def mutate(streets, prob_permute=0.1):
    if random.random() < prob_permute:
        streets = random.shuffle(streets)
    return streets


def perturb(schedule):
    return list(map(mutate, schedule))


def main():
    random.seed(0)
    for basename in 'abcdef':
        # Load data set
        data_set = load(os.path.join('data', f'{basename}.txt'))

        # Create first schedule: rotate evenly
        schedule = []
        for names in data_set.in_streets:
            schedule.append([(name, 1) for name in names])

        # Hill-climb by random steps
        prev_s = score(data_set, schedule)
        for i in tqdm(range(100)):
            new_schedule = perturb(schedule)
            s = score(data_set, new_schedule)
            if s > prev_s:
                schedule = new_schedule

        # Save solution
        out_dir = 'out'
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f'{basename}.txt'), 'w') as f:
            save(schedule, f)


if __name__ == '__main__':
    main()
