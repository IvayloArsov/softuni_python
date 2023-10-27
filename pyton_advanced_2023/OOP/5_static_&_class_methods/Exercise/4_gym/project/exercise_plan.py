class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.id
        ExercisePlan.id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        new_instance = cls(trainer_id, equipment_id, hours * 60)
        return new_instance

    @staticmethod
    def get_next_id():
        return ExercisePlan.id

    def __repr__(self):
        info_str =  f'Plan <{self.id}> with duration {self.duration} minutes'
        return info_str