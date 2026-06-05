import json

class Config:
    def __init__(self, debounce_ms = 5, dot_key = 0, minus_key = 1):
        self.debounce_ms = debounce_ms
        self.dot_key = 0
        self.minus_key = 1
    
    def load():
        try:
            with open('config.json') as stream:
                config = json.load(stream)
            
            return Config(**config)
        except:
            config = Config()
            config.save()
            
            return config
    
    def save(self):
        with open('config.json', 'w') as stream:
            json.dump(self.__dict__, stream)
            
        