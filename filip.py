import collections
import os

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

def get_street_scores(ds):
    street_visits = collections.Counter()
    street_starts = collections.Counter()
    for path in ds.paths:
        # TODO: Weight by car quality.
        street_starts[path[0]] += 1
        for street in path:
            street_visits[street] += 1
    return street_visits, street_starts

def get_s(o):
    if o == 0:
        return 0
    res = int(o / 10)
    if res == 0:
        res += 1
    return res

for basename in 'abcdef':
    print(basename)
    data_set = load(os.path.join('data', f'{basename}.txt'))
    street_visits, street_starts = get_street_scores(data_set)
    #street_scores = {n: get_s(v) for n, v in street_visits.items()}
    schedule = []
    for names in data_set.in_streets:
        #cur_starts = {n: street_starts[n] for n in names}
        #cur_scores = {n: get_s(street_visits[n]) for n in names}
        sched = []
        for n in sorted(names, key=street_starts.__getitem__):
            v = street_visits[n]
            if v == 0:
                continue
            s = get_s(v)
            assert s >= 1
            sched.append((n, s))
        if len(sched) == 0:
            sched = [(names[0], 1)]
        schedule.append(sched)
    out_dir = 'solutions/filip'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f'{basename}.txt'), 'w') as f:
        save(schedule, f)
