from auth_drive import auth_gdrive, Config
from pydrive.drive import GoogleDrive
import pandas as pd
import os

def auth():
    # Authenticates to drive
    cfg = Config()
    gauth = auth_gdrive(client_secrets_path=cfg.credentials.get("google_drive_credentials"))
    drive = GoogleDrive(gauth)
    return drive

def get_folder_id(drive, folder_name, folder_parent='root'):
    fileList = drive.ListFile({'q': f"'{folder_parent}' in parents and trashed=false"}).GetList()
    for file in fileList:
        if(file['title'] == folder_name):
            return file['id']

def dump_drive(drive, folder_id, df, filename, filepath):
    df.to_csv(filepath)
    file = drive.CreateFile({'parents': [{'id': folder_id}], 'title': filename})
    file.SetContentFile(filepath)
    file.Upload()

def get_fileList(drive, folder_parent):
    fileList = drive.ListFile({'q': f"'{folder_parent}' in parents and trashed=false"}).GetList()
    return fileList

def in_folder(fileList, filename):
    fileTitles = [file['title'] for file in fileList]
    return filename in fileTitles

def get_file(drive, id, filepath='aux'):
    file = drive.CreateFile({'id': id})
    file.GetContentFile(filepath)
