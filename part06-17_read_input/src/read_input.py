# Write your solution here
def read_input(str_num, num1, num2):
    while True:
        try:
            number_correct = int(input(f"{str_num}"))
            if number_correct > num1 and number_correct < num2:
                return number_correct
            else:
                print(f"You must type in an integer between {num1} and {num2}")
        except ValueError:
            print(f"You must type in an integer between {num1} and {num2}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 1, 5)
    print("You typed in:", number) 
