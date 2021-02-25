import sys
from solve import load
from matplotlib import pyplot as plt
import numpy as np

file = sys.argv[1]

data = load(file)

street_counts = {}
for path in data.paths:
    for s in path:
        try:
            street_counts[s] += 1
        except:
            street_counts[s] = 1

freqs = np.array(list(street_counts.values()))
fig,ax = plt.subplots(1,1)
ax.hist(freqs, bins = range(0,np.max(freqs)))
ax.set_title(f"{file}")
ax.set_xlabel('frequencies of streets')
ax.set_ylabel('n. of streets')
#plt.show()
plt.savefig(f"{file}".replace('txt', 'png'))


