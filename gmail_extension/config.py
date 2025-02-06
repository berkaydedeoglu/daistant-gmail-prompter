import os
import yaml

class Config:
    def __init__(self, config_file="config.yaml"):
        self.settings = {}
        if os.path.exists(config_file):
            self.__load_from_yaml(config_file)

    def __load_from_yaml(self, config_file):
        try:
            with open(config_file, 'r') as f:
                self.settings = yaml.safe_load(f) or {}
        except Exception as e:
            raise RuntimeError(f"Failed to load configuration from {config_file}: {e}")

    def get(self, section, key, default=None):
        return self.settings.get(section, {}).get(key, default)