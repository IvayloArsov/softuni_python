class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        info_str = f'Category {self.id}: {self.name}'
        return info_str
