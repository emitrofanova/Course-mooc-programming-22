# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{((self.__euros * 100 + self.__cents) / 100):.2f} eur"

    def __eq__(self, another):
        return (self.__euros * 100 + self.__cents) == (another.__euros * 100 + another.__cents)

    def __lt__(self, another):
        return (self.__euros * 100 + self.__cents) < (another.__euros * 100 + another.__cents)
    
    def __gt__(self, another):
        return (self.__euros * 100 + self.__cents) > (another.__euros * 100 + another.__cents)
    
    def __ne__(self, another):
        return (self.__euros * 100 + self.__cents) != (another.__euros * 100 + another.__cents)

    def __add__(self, another):
        new_money = Money(self.__euros, self.__cents)
        new_money.__euros += another.__euros
        new_money.__cents += another.__cents
        return new_money
    
    def __sub__(self, another):
        if another < self:
            new_money = Money(self.__euros, self.__cents)
            new_money.__euros -= another.__euros
            new_money.__cents -= another.__cents
            return new_money
        else:
            raise ValueError("a negative result is not allowed")

if __name__ == "__main__": 
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1