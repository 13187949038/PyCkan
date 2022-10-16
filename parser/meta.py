import json
from posixpath import abspath
import tempfile
import wget
import os
import zipfile
import git
import tinydb
import sqlite3
from tinydb import TinyDB, Query, where
from objprint import objprint
from config_loader import config


# 获取元数据
def get_metadata():
    # tempdir = tempfile.TemporaryDirectory('pyckan_metadata').name
    tempdir = config.Config.load().cache_dir
    
    try:
        os.makedirs(tempdir)
        exists = False
    except:
        exists = True
    
    configs = config.Config.load()

    for source in configs.sources:
        # 不存在
        if not exists:
            print(f'Downloading {source.url}')
            git.Repo.clone_from(source.url, os.path.join(tempdir, source.name))
            print(f'Downloaded {source.url}')
        else:
            print(f'Skip to download {source.url}')
        
        # with zipfile.ZipFile(os.path.join(tempdir, source.name + '.zip')) as zip:
            # zip.extractall(os.path.join(tempdir, source.name))
    
        yield os.path.join(tempdir, source.name)
            

# 分析元数据
def analyse_metadata(meta_dir: str):
    # db = TinyDB('db.json')
    # mod = db.table('mod')
    
    # print(os.listdir(meta_dir))
    
    mod_dirs = [
        os.path.abspath(
            os.path.join(meta_dir, x)
        )
        for x in os.listdir(meta_dir)
        if '.git' not in x
    ]
    
    mod_files = [
        [
            os.path.join(meta_dir, dir, file)
            for file in os.listdir(dir)
            if file.split('.')[-1] == 'ckan'
        ]
        for dir in mod_dirs
        if os.path.isdir(dir)
    ]

    mod_file_contents = []
    
    # 信息处理
    for a in mod_files:
        for file in a:
            with open(file, 'r', encoding='utf-8') as f:
                mod_file_contents.append(
                    json.loads(f.read())
                )
                
    # 数据返回
    return mod_file_contents
                