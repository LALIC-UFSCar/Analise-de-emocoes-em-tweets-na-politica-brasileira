import pandas as pd
import re
import string
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import WhitespaceTokenizer
from drive_utils import auth, get_folder_id, dump_drive, get_file
import sys, os
from yaml import safe_load

nltk.download('stopwords',quiet=True)
nltk.download('averaged_perceptron_tagger',quiet=True)
nltk.download('wordnet',quiet=True)
nltk.download('vader_lexicon',quiet=True)
nltk.download('punkt', quiet = True)

class Config_infos:
    def __init__(self, config_path='../config.yaml'):
        with open(config_path) as f:
            self.complete = safe_load(f)
            self.scripts = self.complete.get("scripts")
            self.clean_dataset = self.scripts.get('clean_dataset')
            self.from_drive = self.clean_dataset.get('from_drive')
            self.file_id = self.clean_dataset.get('file_id')
            self.column_name = self.clean_dataset.get('column_name')
            self.local_path = self.clean_dataset.get('local_path')
            self.folder_id = self.clean_dataset.get('folder_id')
            self.complete_clean = self.clean_dataset.get('complete_clean')

class Clean_dataset:
    def __init__(self, df):
        self.df = df

    def remove_noise(self, sentence):
        sentence = re.sub(r'^RT[\s]+', '', str(sentence))
        sentence = re.sub(r"(?:\@|https?\://)\S+", "", str(sentence))
        sentence = re.sub("\n"," ", sentence)
        return sentence

    def clean_text(self, text):
        text = text.lower()
        text = [word.strip(string.punctuation) for word in text.split(" ")]
        text = [word for word in text if not any(c.isdigit() for c in word)]
        stop = stopwords.words('portuguese')
        lista = ['eh', 'ta', 'tá', 'to', 'tô', 'pro', 'pra', 'nao', 'né', 'ne', 'hein', 'tao', 'tão', 'ai', 'aí', 'ser', 'vai', 'ir', 'ia']
        for e in lista:
          stop.append(e)
        stop.append([])
        text = [x for x in text if x not in stop]
        text = [t for t in text if len(t) > 1]
        text = " ".join(text)
        return(text)

    def clean_dataset(self, column_name, complete_clean):
        try:
            self.df.drop(columns=['Unnamed: 0'], inplace=True)
        except KeyError:
            pass
        self.df[column_name] = self.df[column_name].apply(lambda x: self.remove_noise(str(x)))
        if complete_clean:
            self.df[column_name] = self.df[column_name].apply(lambda x: self.clean_text(str(x)))
        self.df.dropna(inplace=True)
        self.df.reset_index(inplace=True)


if __name__ == '__main__':
    cfg = Config_infos()
    drive = auth()

    if cfg.from_drive:
        get_file(drive, cfg.file_id, cfg.local_path)
    df = pd.read_csv(cfg.local_path)

    dataset = Clean_dataset(df)
    dataset.clean_dataset(cfg.column_name, cfg.complete_clean)

    filepath_clean = cfg.local_path.split('.csv')[0] + '_clean.csv'
    filename_clean = filepath_clean.split('/')[-1]
    dump_drive(drive, cfg.folder_id, df, filename_clean, filepath_clean)
