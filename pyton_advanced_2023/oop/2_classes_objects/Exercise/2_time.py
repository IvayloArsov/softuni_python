class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours: int, new_minutes: int, new_seconds: int):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        curr_time = f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
        return curr_time

    def next_second(self):
        self.seconds = (self.seconds + 1) % (Time.max_seconds + 1)
        if self.seconds == 0:
            self.minutes = (self.minutes + 1) % (Time.max_minutes + 1)
            if self.minutes == 0:
                self.hours = (self.hours + 1) % (Time.max_hours + 1)
        return self.get_time()

    # def next_second(self):
    #     next_second = self.seconds + 1
    #     if next_second > Time.max_seconds:
    #         self.seconds = 0
    #         next_minute = self.minutes + 1
    #         if next_minute > Time.max_minutes:
    #             self.minutes = 0
    #             next_hour = self.hours + 1
    #             if next_hour > Time.max_hours:
    #                 self.hours = 0
    #             else:
    #                 self.hours += 1
    #         else:
    #             self.minutes += 1
    #     else:
    #         self.seconds += 1
    #     return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
