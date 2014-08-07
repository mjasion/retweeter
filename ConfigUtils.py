import os
import ConfigParser
import inspect
import re


class ConfigUtils(object):
    def __init__(self):
        path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # read config
        config = ConfigParser.SafeConfigParser()
        config.read(os.path.join(path, "config"))
        self.config = config

    def get(self, group, key):
        return self.config.get(group, key).strip()

    def read_list(self, group, key):
        config_value = self.config.get(group, key).strip()
        return re.split('\s*,\s*', config_value)