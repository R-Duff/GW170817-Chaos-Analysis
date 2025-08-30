import numpy as np
import nolds

def compute_lle(signal, emb_dim=10, lag=5, min_tsep=10):
    return nolds.lyap_r(signal, emb_dim=emb_dim, lag=lag, min_tsep=min_tsep)

def box_count(signal, box_sizes):
    counts = []
    for size in box_sizes:
        min_signal, max_signal = np.min(signal), np.max(signal)
        bins = np.arange(min_signal, max_signal, size)
        digitized = np.digitize(signal, bins)
        unique_boxes = np.unique(digitized)
        counts.append(len(unique_boxes))
    return counts

def fractal_dimension_boxcount(signal, min_box_size=0.001, max_box_size=0.1, num_sizes=20):
    box_sizes = np.logspace(np.log10(min_box_size), np.log10(max_box_size), num=num_sizes)
    counts = box_count(signal, box_sizes)
    coeffs = np.polyfit(np.log(box_sizes), np.log(counts), 1)
    return -coeffs[0]
