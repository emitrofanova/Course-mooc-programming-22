# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.c_num = 0

    def add_number(self, number:int):
        self.numbers += number
        self.c_num += 1

    def count_numbers(self):
        return self.c_num
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        if self.numbers == 0:
            return 0
        return self.numbers / self.c_num


print("Please type in integer numbers:")
stats = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()
while True:
    numb = int(input())
    if numb == -1:
        break
    elif numb % 2 == 0:
        stats_even.add_number(numb)
    else:
        stats_odd.add_number(numb)
    stats.add_number(numb)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats_even.get_sum())
print("Sum of odd numbers:", stats_odd.get_sum())
