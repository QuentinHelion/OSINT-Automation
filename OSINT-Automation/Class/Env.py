import os
from dotenv import load_dotenv

class Env:
    def __init__(self, path):
        self.path = path
        self.load_env()

    def load_env(self):
        load_dotenv(self.path)

    def get_var(self, var_name):
        return os.getenv(var_name)
