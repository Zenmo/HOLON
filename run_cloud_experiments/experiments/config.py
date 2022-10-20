from pathlib import Path
import yaml


class Config(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def load(cls, path):
        with open(path, 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
        return cls(doc)

config = Config.load(Path(__file__).parent.parent / 'config/config.yml')
