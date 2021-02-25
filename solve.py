#!/usr/env/bin python3

import os

from attributedict.collections import AttributeDict


def load(filename):
    streets = {}
    bs = []
    es = []
    ls = []
    paths = []
    with open(filename) as f:
        D, I, S, V, F = map(int, f.readline().split())
        for i in range(S):
            B, E, name, L = f.readline().split()
            B = int(B)
            E = int(E)
            L = int(L)
            streets[name] = (B, E, L)
            bs.append(B)
            es.append(E)
            ls.append(L)
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


def main():
    for basename in 'abcdef':
        data_set = load(os.path.join('data', f'{basename}.txt'))
        schedule = []
        out_dir = 'out'
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f'{basename}.txt'), 'w') as f:
            save(schedule, f)
    # Create a simple solution: all interesctions rotate evenly
    # Evaluate the solution


if __name__ == '__main__':
    main()
