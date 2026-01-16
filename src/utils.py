import os

def get_allDirNames(dir):
    dir_names = [
        f for f in os.listdir(dir) if os.path.isdir(os.path.join(dir, f))
    ]
    return dir_names

def get_allCsvNames(dir):
    csv_files = [
        f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and f.endswith('.csv')
    ]
    return csv_files

# path: 'root' or 'csv'  or 'proc'
def get_staticPath(path):
    root = os.getcwd()
    csv_dir = os.path.join(root, 'data', 'csv')
    proc_dir = os.path.join(root, 'data', 'proc')
    dict = {'root' : root, 'csv' : csv_dir, 'proc': proc_dir}
    return dict[path]