class Clock:
    # constructor
    def __init__(self, hours: int, minutes: int) -> None:                          
        self.hours = hours
        self.minutes = minutes
        self.normal_time()

    def normal_time(self) -> None:
        total_mins = int((self.hours * 60) + self.minutes)
        hours = int(total_mins // 60)
        if hours >= 24:
            hours = hours % 24
        minutes = total_mins % 60
        str_min = str(minutes)
        if minutes < 10:
            str_min = str(0) + str_min
        self.hours, self.minutes = int(hours), int(str_min)

    def __eq__(self, other: object) -> bool:
        # if self and other are of different, incompatible types, they are not equal
        if not isinstance(other, Clock):  
            return NotImplemented
        if self.hours == other.hours and self.minutes == other.minutes:
            return True
        else:
            return False
    
    def __add__(self, other: "Clock") -> "Clock":
        total_obj = Clock(self.hours + other.hours, self.minutes + other.minutes)
        return total_obj
    
    def add_minutes(self, minutes: int) -> "Clock":
        self.minutes += minutes
        self.normal_time()
        return self
    
    def __str__(self) -> str:
        self.normal_time()
        time = "{}:{}".format(self.hours, self.minutes)
        return time


if __name__ == "__main__":
    t1 = Clock(0, 0)
    t2 = Clock(68, 89)
    print(t1 == t2)
    print(t1 + t2)
    print(t1.add_minutes(180))
    print(t1.__str__())
    print(t1.hours)
    print(t1.minutes)