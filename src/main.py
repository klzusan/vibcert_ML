import utils as ut
import csv_handler as ch
import preProc as pp
import matplotlib.pyplot as plt

persons_name = ut.get_allDirNames(ut.get_staticPath('csv'))
for person in persons_name:
    for n1 in range(1, 2):
        for n2 in range(1, 7):
            # 各csvファイルをロード
            csv = ch.load_csv('r', person, n1, n2)

            # 前処理したデータをdata/procに保存
            