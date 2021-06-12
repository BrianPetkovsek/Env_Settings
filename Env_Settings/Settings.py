import os
from os.path import join, dirname
from dotenv import load_dotenv

class Settings_:
    def __init__(self, dotenv_path: str = join(os.getcwd(), '.env')):
        self.reload_env(dotenv_path)

    def reload_env(self, dotenv_path: str):
        A = dict(os.environ).copy()
        load_dotenv(dotenv_path, override=True)
        C = {k:v for k,v in dict(os.environ).items() if k not in A}
        self.update_tokens(C)
    
    def update_tokens(self, tokens: dict):
        for k,i in tokens.items():
            os.putenv(k, str(i))
        self.__dict__ = dict(self.__dict__, **tokens)

    def set_access_token(self, key: str, value: str):
        import os
        if not self.has_access_token(key):
            with open(".env", "a") as f:
                f.write(f'{key}={str(value)}\n')

        self.update_tokens({key: value})

    def has_access_token(self, key):
        return key in self.__dict__.keys() and self.__dict__[key] is not None and self.__dict__[key] is not ''

Settings = Settings_()

if __name__ == '__main__':
    print(Settings.__dict__)
    