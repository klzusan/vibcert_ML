import os
import pandas as pd

import utils as ut

# type: 'r'(row) or 'p'(preProcessed) or 'o'(original)
def load_csv(type, person_name, n1, n2):
    # 各csvファイルごとに呼び出される

    if type == 'o':
        file_path = os.path.join(ut.get_staticPath('original'), person_name, f'vibCert_{n1}_{n2}.csv')
    elif type == 'p':
        file_path = os.path.join(ut.get_staticPath('proc'), person_name, f'processed_{n1}_{n2}.csv')
    elif type == 'r':
        file_path = os.path.join(ut.get_staticPath('raw'), person_name, f'raw_{n1}_{n2}.csv')

    df = pd.read_csv(file_path)
    return df

def write_csv(type, person_name, n1, n2, df):
    if type == 'p':
        dir = os.path.join(ut.get_staticPath('proc'), person_name)
        if not os.path.exists(dir):
            os.mkdir(dir)
        file_path = os.path.join(dir, f'processed_{n1}_{n2}.csv')

    print(file_path)
    df.to_csv(file_path)