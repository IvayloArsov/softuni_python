class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.id
        Equipment.id += 1

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self):
        info_str = f'Equipment <{self.id}> {self.name}'
        return info_str
