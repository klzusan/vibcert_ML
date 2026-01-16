import os
import pandas as pd

import utils as ut

# type: 'r'(row) or 'p'(preProcessed)
def load_csv(type, person_name, n1, n2):
    # 各csvファイルごとに呼び出される

    if type == 'r':
        file_path = os.path.join(ut.get_staticPath('csv'), person_name, f'vibCert_{n1}_{n2}.csv')
    elif type == 'p':
        file_path = os.path.join(ut.get_staticPath('proc'), person_name, f'processed_{n1}_{n2}.csv')

    

    df = pd.read_csv(file_path)
    return df