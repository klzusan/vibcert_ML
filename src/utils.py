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

# path: 'root' or 'original' or 'raw'  or 'proc' or 'img_ori' or 'img_raw' or 'img_proc'
def get_staticPath(path):
    root = os.getcwd()
    raw_dir = os.path.join(root, 'data', 'raw')
    proc_dir = os.path.join(root, 'data', 'proc')
    img_procDir = os.path.join(root, 'output_img', 'proc')
    img_rawDir = os.path.join(root, 'output_img', 'raw')
    ori_dir = os.path.join(root, 'data', 'original')
    img_oriDir = os.path.join(root, 'output_img', 'original')
    dict = {
        'original' : ori_dir,
        'root' : root,
        'raw' : raw_dir,
        'proc': proc_dir,
        'img_ori' : img_oriDir,
        'img_raw' : img_rawDir,
        'img_proc' : img_procDir,
    }
    return dict[path]