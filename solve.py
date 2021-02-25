#!/usr/env/bin python3

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


def main():
    for basename in 'abcdef':
        print(load(f'{basename}.txt'))
    # Create a simple solution: all interesctions rotate evely
    # Save the solution
    # Evaluate the solution


if __name__ == '__main__':
    main()
