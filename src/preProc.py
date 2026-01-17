from scipy import signal
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd

def proc_norm(raw_segments):
    # 標準化
    scaler = StandardScaler()
    normalized_segments = []

    for seg in raw_segments:
        normalized_segments.append(scaler.fit_transform(seg))

    normalized_segments = np.array(normalized_segments)

    return normalized_segments

def lowpass(data, cutoff=10, fs=50, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    processed = signal.filtfilt(b, a, data, axis=0)
    processed_df = pd.DataFrame(
        processed,
        columns=data.columns,
        index=data.index
    )
    return processed_df

def make_windows(data, window_size=50, overlap=30):
    print(f"Window size: {window_size}, Overlap: {overlap}", end="")
    segments = []
    for i in range(0, len(data) - window_size + 1, window_size - overlap):
        window = data.iloc[i : i + window_size]
        segments.append(window)
    return np.array(segments)