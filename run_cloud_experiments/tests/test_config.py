from experiments.config import config

def test_config():
    assert config['anylogic_cloud']
    assert config['anylogic_cloud']['url']
    assert config['anylogic_cloud']['api_key']
