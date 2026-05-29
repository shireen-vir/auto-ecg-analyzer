"""
Auto ECG Analyzer utility functions.

This module contains various utility functions used in the auto-ecg-analyzer tool.
It provides functions for data preprocessing, feature extraction, and other tasks.
"""

import numpy as np
import pandas as pd
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def main():
    # Example usage of the butter_bandpass_filter function
    fs = 100.0
    lowcut = 0.5
    highcut = 30.0
    t = np.linspace(0, 1, int(fs), endpoint=False)
    data = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
    filtered_data = butter_bandpass_filter(data, lowcut, highcut, fs)
    print(filtered_data)

if __name__ == "__main__":
    main()