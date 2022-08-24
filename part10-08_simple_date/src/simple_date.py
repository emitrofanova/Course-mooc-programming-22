# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.date = date
        self.month = month
        self.year = year

    def __lt__(self, another):
        return (self.year * 360 + self.month * 30 + self.date) < (another.year * 360 + another.month * 30 + another.date)

    def __gt__(self, another):
        return (self.year * 360 + self.month * 30 + self.date) > (another.year * 360 + another.month * 30 + another.date)

    def __eq__(self, another):
        return (self.year * 360 + self.month * 30 + self.date) == (another.year * 360 + another.month * 30 + another.date)

    def __ne__(self, another):
        return (self.year * 360 + self.month * 30 + self.date) != (another.year * 360 + another.month * 30 + another.date)
    
    def __str__(self):
        return f"{self.date}.{self.month}.{self.year}"

    def __add__(self, another):
        new_date = SimpleDate(self.date, self.month, self.year)
        new_date.year += another // 360
        new_date.month += (another % 360) // 30
        new_date.date += (another % 360) % 30
        if new_date.date > 30:
            new_date.month += new_date.date // 30
            new_date.date = new_date.date % 30
        if new_date.month > 12:
            new_date.year += new_date.month // 12
            new_date.month = new_date.month % 12
        return new_date

    def __sub__(self, another):
        return abs((self.year * 360 + self.month * 30 + self.date) - (another.year * 360 + another.month * 30 + another.date))

if __name__ == "__main__": 
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
