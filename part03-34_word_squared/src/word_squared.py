# Write your solution here
def squared(name, num):
    st = name * num * num
    i = 0
    j = 1
    while j <= num:
        print(st[i:i + num])
        i += num
        j += 1

if __name__ == "__main__":
    squared("ab", 3)