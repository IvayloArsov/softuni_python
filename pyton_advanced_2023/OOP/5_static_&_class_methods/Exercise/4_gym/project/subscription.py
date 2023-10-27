class Subscription:
    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.id = Subscription.id
        Subscription.id += 1
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

    def __repr__(self):
        info_str = f'Subscription <{self.id}> on {self.date}'
        return info_str

    @staticmethod
    def get_next_id():
        return Subscription.id
