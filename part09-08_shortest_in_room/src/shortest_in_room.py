# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return self.persons == []
    
    def print_contents(self):
        answ = f"There are {len(self.persons)} in the room, and their combined height is "
        sum_height = 0
        answ2 = ""
        for person in self.persons:
            sum_height += person.height
            answ2 += f"{person.name} ({person.height} cm)\n"
        answ += str(sum_height) + " cm\n" + answ2
        print(answ[:-1])

    def shortest(self):
        if not self.is_empty():
            min_height = self.persons[0].height
            answ = self.persons[0]
            for person in self.persons:
                if person.height < min_height:
                    min_height = person.height
                    answ = person
            return answ
        else:
            return None

    def remove_shortest(self):
        if not self.is_empty():
            rem = self.shortest()
            self.persons.remove(rem)
            return rem
        else:
            return None

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
