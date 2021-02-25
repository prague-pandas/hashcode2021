from solve import load, save
import os



for basename in 'abcdef':
    data_set = load(os.path.join('data', f'{basename}.txt'))
    street_counts = {}
    for path in data_set.paths:
        for s in path:
            try:
                street_counts[s] += 1
            except:
                street_counts[s] = 1
    schedule = []
    for names in data_set.in_streets:
        freqs = {}
        for s in names:
            try:
                freqs[s] = street_counts[s]
            except:
                freqs[s] = 1
        #min_freq = min(freqs.values())
        schedule.append([(name, int(freqs[name])) for name in names])
    out_dir = 'solutions/rotate-according-to-frequencies'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f'{basename}.txt'), 'w') as f:
        save(schedule, f)
