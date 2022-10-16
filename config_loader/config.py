import json
import re
from typing import List


class Source:
    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url

    def url_check(self):
        if re.findall(r"https?\:\/\/.*", self.url).__len__() == 1:
            return True
        else:
            return False

    def dump(self):
        return {
            'name': self.name,
            'url': self.url,
            'check': self.url_check()
        }

    @staticmethod
    def load(data: dict):
        return Source(
            name=data['name'],
            url=data['url']
        )


class Config(dict):
    def __init__(self, refresh_data_on_launch: bool, cache_dir: str, sources: list[Source]):
        self.refresh_data_on_launch = refresh_data_on_launch
        self.cache_dir = cache_dir

        self.sources: list[Source] = sources

        # url 规范性检查
        # for source in sources:
            # if source.url_check() == False:
                # raise ValueError('不符合规范的 URL')

    def __getitem__(self, __key):
        if __key == 'refresh_data_on_launch':
            return self.refresh_data_on_launch
        elif __key == 'cache_dir':
            return self.cache_dir
        elif __key == 'sources':
            return self.sources
        else:
            raise KeyError('错误的设置键')

    def __setitem__(self, __key, __value):
        if __key == 'refresh_data_on_launch':
            self.refresh_data_on_launch = __value
        elif __key == 'cache_dir':
            self.cache_dir == __value
        elif __key == 'sources':
            # 规范性检查
            for source in __value:
                if source.url_check() == False:
                    raise ValueError('不符合规范的 URL')
                
            # 赋值
            self.sources = __value

        self.save()

    def dump(self):
        return {
            'refresh_data_on_launch': self.refresh_data_on_launch,
            'cache_dir': self.cache_dir,
            'sources': [x.dump() for x in self.sources]
        }

    def save(self):
        with open('./pyckan.config.json', 'w', encoding='utf-8') as f:
            f.write(
                json.dumps(self.dump())
            )
        
    @staticmethod
    def load():
        try:
            with open('./pyckan.config.json', 'r', encoding='utf-8') as f:
                data = json.loads(f.read())
                
                return Config(
                    refresh_data_on_launch=data['refresh_data_on_launch'],
                    cache_dir=data['cache_dir'],
                    sources=[Source.load(src) for src in data['sources']]
                )
        except FileNotFoundError or KeyError:
            Config(
                refresh_data_on_launch=True,
                cache_dir='/tmp',
                sources=[]
            ).save()


if '__main__' == __name__:
    sources = [
        Source('aaa', 'http://example.com')
    ]
    
    cfg1 = Config(True, '/tmp', sources)
    
    print(cfg1.dump())
