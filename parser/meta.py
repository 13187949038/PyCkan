import tempfile
import wget
import os
import zipfile
import git
from objprint import objprint
from config_loader import config


def get_metadata():
    tempdir = tempfile.TemporaryDirectory('pyckan_metadata').name
    
    try:
        os.makedirs(tempdir)
    except:
        pass
    
    configs = config.Config.load()

    for source in configs.sources:
        print(f'Downloading {source.url}')
        git.Repo.clone_from(source.url, os.path.join(tempdir, source.name))
        print(f'Downloaded {source.url}')
        
        # with zipfile.ZipFile(os.path.join(tempdir, source.name + '.zip')) as zip:
            # zip.extractall(os.path.join(tempdir, source.name))
            