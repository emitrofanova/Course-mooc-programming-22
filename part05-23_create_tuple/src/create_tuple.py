# Write your solution here
def create_tuple(x: int, y: int, z: int):
    values = [x, y, z]
    min_value = min(values)
    max_value = max(values)
    sum_value = sum(values)
    return (min_value, max_value, sum_value)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
