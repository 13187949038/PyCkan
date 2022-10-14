from config_loader import config


def test_source():
    assert config.Source('test', 'abc').url_check() == False
    assert config.Source('test2', 'http://example.com').url_check() == True


def test_config():
    sources = [
        config.Source('aaa', 'http://example.com')
    ]
    
    cfg1 = config.Config(True, '/tmp', sources)
    
    assert cfg1['refresh_data_on_launch'] == True
    assert cfg1['cache_dir'] == '/tmp'
    assert cfg1['sources'] == sources
    assert cfg1.dump() == {'refresh_data_on_launch': True, 'cache_dir': '/tmp', 'sources': [{'name': 'aaa', 'url': 'http://example.com', 'check': True}]}
    