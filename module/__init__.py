import hashlib
import os
import wget
import zipfile
import datetime
from config_loader import config


class Tag:
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = hashlib.md5(self.name.encode('utf-8')).hexdigest()


class Resource:
    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url
        self.id = hashlib.md5(
            f'{self.name}{self.url}'.encode('utf-8')).hexdigest()


class CKANModule(object):
    def __init__(self, name: str,
                 abstract: str,
                 author: list[str],
                 depends: list[object],
                 download: str, download_content_type: str,
                 download_hash_sha1: str,
                 download_hash_sha256: str,
                 identifier: str,
                 install: list[dict],
                 ksp_version_max: str,
                 ksp_version_min: str,
                 localizations: str,
                 recommends: list[object],
                 release_date: str,
                 resources: list[Resource],
                 suggest: list[object],
                 tags: list[Tag],
                 version: str
                 ) -> None:
        self.name = name
        self.abstract = abstract
        self.author = author
        self.depends = depends
        self.download = download
        self.download_hash_sha1 = download_hash_sha1
        self.download_hash_sha256 = download_hash_sha256
        self.identifier = identifier
        self.install = install
        self.ksp_version_max = ksp_version_max
        self.ksp_version_min = ksp_version_min
        self.localizations = localizations
        self.recommends = recommends
        self.release_date = datetime.datetime.fromisoformat(release_date)
        self.resources = resources
        self.suggest = suggest
        self.tags = tags
        self.version = version

    def download_module(self):
        cfg = config.Config.load()
        module_zip_filename = os.path.abspath(
            os.path.join(cfg.cache_dir, self.name + '.zip')
        )

        # 存在即跳过
        if os.path.exists(module_zip_filename):
            return module_zip_filename

        wget.download(self.download, module_zip_filename)

        return module_zip_filename

    def install_module(self):
        # 解压文件
        with zipfile.ZipFile(
            self.download_module()
        ) as zip:
            # TODO: 安装    Install
            pass


# REPL
if '__main__' == __name__:
    # a = CKANModule()
    tag_a = Tag('test')
    resource_a = Resource('github', 'https://github.com/13187949038')

    print(tag_a.id)
    print(resource_a.id)
