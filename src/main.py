import utils as ut
import plt_utils as pu
import csv_handler as ch
import preProc as pp
import matplotlib.pyplot as plt
import numpy as np
import os
import ml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score

# モーションの数
MOTION_NUM = 6

persons_name = ut.get_allDirNames(ut.get_staticPath('original'))

# features_set: ['モーション番号', {'名前A':特徴量, '名前B':特徴量, ...}]
features_set = [[] for _ in range(MOTION_NUM)]
for i in range(0, MOTION_NUM):
    features_set[i].append(i+1)
    features_set[i].append({})

for person in persons_name:
    print(f'Processing: {person}')
    for n1 in range(1, 2):
        for n2 in range(1, MOTION_NUM + 1):
            # 現在は静止モーション（1-1と1-2）だけ扱う
            if n2 != 1 and n2 != 2: 
                break
            print(f"{n1}-{n2} ", end="")

            # 各csvファイルをロード
            ori = ch.load_csv('o', person, n1, n2)

            # 可視化して~/output_img/original/にpngとして保存
            # pu.visual_data(ori, 'ori', person, n1, n2)

            # ローパスフィルタをかける
            temp_filt = pp.lowpass(ori)

            # データインデックスの100~399の部分を切り出す
            temp_data = temp_filt.loc[100:399]

            # 可視化して~/output_img/raw/にpngとして保存
            # pu.visual_data(temp_data, 'raw', person, n1, n2)

            # データをスライディングウィンドウにより分ける
            raw_segments = pp.make_windows(temp_data)
            print(f", Segment size: {len(raw_segments)}")

            # 標準化
            norm = pp.proc_norm(raw_segments)
            # pu.visual_seg(norm, person, n1, n2)

            # 特徴量抽出
            features = ml.extract_features(norm)
            features_set[n2-1][1][person] = features

# ここまでで特徴量抽出完了

# ラベル付け(ここから疲れたからテキトー)
label_X1 = []
label_X2 = []
for i in range(0, 9):
    label_X1.append(features_set[0][1][persons_name[i]])
    label_X2.append(features_set[1][1][persons_name[i]])
X1 = np.vstack(label_X1)
X2 = np.vstack(label_X2)

sum_y1 = []
sum_y2 = []
for j in range(0, 9):
    sum_y1 += ([j+1] * len(features_set[0][1][persons_name[j]]))
    sum_y2 += ([j+1] * len(features_set[1][1][persons_name[j]]))
y1 = np.array(sum_y1)
y2 = np.array(sum_y2)

# 学習用と検証用に分割
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, stratify=y1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, stratify=y2)

# ランダムフォレストで学習
clf1 = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
clf2 = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)

# 検証
y1_pred = clf1.predict(X1_test)
y2_pred = clf2.predict(X2_test)

print("--- Motion 1 Evaluation ---")
print(classification_report(y1_test, y1_pred, target_names=persons_name, zero_division=0))
# 個別に数値として取得したい場合
f1_motion1 = f1_score(y1_test, y1_pred, average='macro') # 全クラスの平均F値
print(f"Motion 1 Macro F1-score: {f1_motion1:.4f}")

# --- モーション2 (n2=2) の評価 ---
print("\n--- Motion 2 Evaluation ---")
print(classification_report(y2_test, y2_pred, target_names=persons_name, zero_division=0))
# 個別に数値として取得したい場合
f1_motion2 = f1_score(y2_test, y2_pred, average='macro') # 全クラスの平均F値
print(f"Motion 2 Macro F1-score: {f1_motion2:.4f}")