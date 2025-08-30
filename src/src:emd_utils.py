import numpy as np
from PyEMD import EMD

def apply_emd(signal):
    emd = EMD()
    IMFs = emd.emd(signal)
    return IMFs

def normalize(signal):
    return (signal - np.mean(signal)) / np.std(signal)
