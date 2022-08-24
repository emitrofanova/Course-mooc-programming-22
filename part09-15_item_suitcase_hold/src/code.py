# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__curr_items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() < self.__max_weight:
            self.__curr_items.append(item)

    def __str__(self):
        if len(self.__curr_items) == 1:
            return f"{len(self.__curr_items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__curr_items)} items ({self.weight()} kg)"

    def print_items(self):
        for item in self.__curr_items:
            print(item)

    def weight(self):
        curr_weight = 0
        for item in self.__curr_items:
            curr_weight += item.weight()
        return curr_weight

    def heaviest_item(self):
        heaviest = self.__curr_items[0].weight()
        answ = self.__curr_items[0]
        if self.__curr_items != []:
            for item in self.__curr_items:
                if item.weight() > heaviest:
                    heaviest = item.weight()
                    answ = item
            return answ
        else:
            return None

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__curr_items = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() < self.__max_weight:
            self.__curr_items.append(suitcase)

    def weight(self):
        curr_weight = 0
        for item in self.__curr_items:
            curr_weight += item.weight()
        return curr_weight

    def __str__(self):
        if len(self.__curr_items) == 1:
            return f"{len(self.__curr_items)} suitcase, space for {self.__max_weight - self.weight()} kg"
        else:
            return f"{len(self.__curr_items)} suitcases, space for {self.__max_weight - self.weight()} kg"

    def print_items(self):
        for suitcase_ in self.__curr_items:
            suitcase_.print_items()

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
