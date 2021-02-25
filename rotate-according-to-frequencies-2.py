from solve import load, save
import os

def count_streets_in_paths(data_set):
    street_counts = {}
    for path in data_set.paths:
        for s in path:
            try:
                street_counts[s] += 1
            except:
                street_counts[s] = 1
    return street_counts

def count_streets_in_paths_2(data_set):
    street_counts = {}
    for path in data_set.paths:
        for i, s in enumerate(path):
            try:
                street_counts[s] += len(path) - i
            except:
                street_counts[s] = len(path) - i
    return street_counts

for basename in 'abcdef':
    print(basename)
    data_set = load(os.path.join('data', f'{basename}.txt'))
    street_counts = count_streets_in_paths_2(data_set)
    schedule = []
    for names in data_set.in_streets:
        priorities = {}
        for s in names:
            try:
                priorities[s] = street_counts[s] / data_set.streets_lens[s]
            except:
                pass
        if priorities:
            min_p = min(priorities.values())
            for s in priorities:
                priorities[s] = priorities[s] / min_p
            priorities_sorted = sorted(priorities, key=priorities.__getitem__)
            #for i, s in enumerate(priorities_sorted):
            #    priorities[s] = i + 1
            schedule.append(
                [(name, int(priorities[name])) for name in
                 reversed(priorities_sorted)])
        else:
            schedule.append([(name, 1) for name in names])
    out_dir = 'solutions/rotate-according-to-frequencies-2'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f'{basename}.txt'), 'w') as f:
        save(schedule, f)
