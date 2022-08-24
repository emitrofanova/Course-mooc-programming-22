# Write your solution here:
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def tick(self):
        if self.seconds == 59:
            if self.minutes == 59:
                if self.hours == 23:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                else:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
            else:
                self.seconds = 0
                self.minutes += 1
        else:
            self.seconds += 1

    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
