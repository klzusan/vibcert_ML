import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def extract_features(segments):
    # 軸(ax~gz)ごとに特徴量を抽出
    all_features = []
    for s in segments:
        f = []
        for i in range(6):
            # ある軸を取り出す
            axis_data = s[:, i]

            f.append(np.mean(axis_data))
            f.append(np.std(axis_data))
            f.append(np.max(axis_data) - np.min(axis_data))
            f.append(np.sum(np.abs(np.diff(axis_data))))
        all_features.append(f)

    return np.array(all_features)