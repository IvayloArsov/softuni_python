class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.id
        Trainer.id += 1

    def __repr__(self):
        info_str = f'Trainer <{self.id}> {self.name}'
        return info_str

    @staticmethod
    def get_next_id():
        return Trainer.id
