# Write your solution here
def layers(num: int):
    ABC = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J",
     11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T",
     21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}
    answ = []
    for i in range(num):
        line = ABC[num-i]*(num * 2 - 1)
        answ.append(line)
        answ[i] = answ[i-1][0:i] + line[i:(num*2-1-i)] + answ[i-1][(num*2-1-i):]
        print(answ[i])
    for i in range(2, num + 1):
        print(answ[num - i])

number = int(input("Layers: "))
layers(number)
