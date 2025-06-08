
import numpy as np
import pandas as pd

def get_valuation(data, stages):
    valuation = {}
    for stage in stages:
        valuation[stage] = {}
        k = data['stage']==stage
        x = np.unique(data['valuation'][k].to_numpy(), return_counts=True)
        valuation[stage]['values'] = x[0]
        valuation[stage]['probabilities'] = x[1]/np.sum(x[1])
    return valuation

def get_ownership(data, stages):
    ownership = {}
    for stage in stages:
        ownership[stage] = {}
        k = data['stage']==stage
        x = data['ownership'][k].to_numpy()
        values = np.append(x,np.array([1.]))
        x = data['quantile'][k].to_numpy()
        probabilities = np.diff(np.append(np.array([0.]),np.append(x,np.array([1.]))))
        ownership[stage]['values'] = values
        ownership[stage]['probabilities'] = probabilities
    return ownership
