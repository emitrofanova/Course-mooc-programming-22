# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
    
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, sum_depos):
        if sum_depos < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        else:
            self.balance += sum_depos


card_Peter = LunchCard(20)
card_Grace = LunchCard(30)
card_Peter.eat_special()
card_Grace.eat_lunch()
print("Peter: ", end='')
print(card_Peter)
print("Grace: ", end='')
print(card_Grace)
card_Peter.deposit_money(20)
card_Grace.eat_special()
print("Peter: ", end='')
print(card_Peter)
print("Grace: ", end='')
print(card_Grace)
card_Peter.eat_lunch()
card_Peter.eat_lunch()
card_Grace.deposit_money(50)
print("Peter: ", end='')
print(card_Peter)
print("Grace: ", end='')
print(card_Grace)
