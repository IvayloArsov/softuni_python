class Song:

    def __init__(self, name: str, length: float, single=False):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        info_str = f'{self.name} - {self.length}'
        return info_str
