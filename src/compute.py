
import numpy as np

def simulate_ownership(ownership, valuation, stages, size=1, seed=777):

    np.random.seed(seed)
    samples = {}
    for stage in stages:
        samples[stage] = {}
        values = ownership[stage]['values']
        probabilities = ownership[stage]['probabilities']
        buckets = np.diff(np.append([0.],values))
        i = np.random.choice(len(values), size=size, p=probabilities)
        n = np.random.rand(size)
        x = values[i]-buckets[i]*n
        values = valuation[stage]['values']
        probabilities = valuation[stage]['probabilities']
        y = np.random.choice(values, size=size, p=probabilities)
        samples[stage] = x*y

    return samples

def compute_stats(samples, stages, quantiles={'10th':0.1,'25th':0.25,'50th':0.5,'75th':0.75,'90th':0.9}):

    q = list(quantiles.values())
    stats = dict.fromkeys(list(quantiles.keys())+['Mean'], [])
    for stage in stages:
        for quantile in quantiles:
            stats[quantile] = stats[quantile]+[float(np.quantile(samples[stage], quantiles[quantile]))]
        stats['Mean'] = stats['Mean']+[float(np.mean(samples[stage]))]

    return stats
