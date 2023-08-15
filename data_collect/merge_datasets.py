from drive_utils import auth, get_folder_id, get_fileList, dump_drive, get_file
import pandas as pd
from os import listdir
from os.path import isfile, join
from yaml import safe_load

class Config_infos:
    def __init__(self, config_path='../config.yaml'):
        with open(config_path) as f:
            self.complete = safe_load(f)
            self.scripts = self.complete.get("scripts")
            self.merge_datasets = self.scripts.get('merge_datasets')
            self.from_drive = self.merge_datasets.get('from_drive')
            self.local_path = self.merge_datasets.get('local_path')
            self.folder_id = self.merge_datasets.get('folder_id')
            self.filename = self.merge_datasets.get('filename')

if __name__ == '__main__':
    cfg = Config_infos()
    drive = auth()

    if cfg.from_drive:
        fileList = get_fileList(drive, cfg.folder_id)
        ids = [file['id'] for file in fileList]
        for id in ids:
            get_file(drive, id, cfg.local_path + str(id) + '.csv')

    all_files = [f for f in listdir(cfg.local_path) if isfile(join(cfg.local_path, f))]
    dfs = []
    for file in all_files:
        df = pd.read_csv(cfg.local_path + file)
        dfs.append(df)

    df = pd.concat(dfs)
    df.reset_index(drop=True, inplace=True)
    try:
        df.drop(columns=['Unnamed: 0', 'level_0', 'index'], inplace=True)
    except KeyError:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    filepath = cfg.local_path + cfg.filename
    dump_drive(drive, cfg.folder_id, df, cfg.filename, filepath)
