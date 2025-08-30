import h5py
import numpy as np
from scipy.signal import butter, filtfilt

def load_strain_data(file_path):
    with h5py.File(file_path, 'r') as f:
        strain = f['strain']['Strain'][:]
        dt = f['strain']['Strain'].attrs['Xspacing']
    time = np.arange(len(strain)) * dt
    return strain, time, dt

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low, high = lowcut / nyq, highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

def extract_segment(strain, fs, start_time, end_time):
    start_idx = int(start_time * fs)
    end_idx = int(end_time * fs)
    return strain[start_idx:end_idx]
