import json

class Config:
    def __init__(self, dot_key = 3, minus_key = 2, poll_frequency=1000, in_1=2, in_2=3):
        self.dot_key = dot_key
        self.minus_key = minus_key
        self.poll_frequency = poll_frequency
        self.in_1 = in_1
        self.in_2 = in_2
    
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
            
        