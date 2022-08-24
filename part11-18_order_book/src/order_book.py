# Write your solution here:
class Task:
    id = 0

    @classmethod
    def id_new(cls, id):
        cls.id += 1
        return cls.id

    def __init__(self, description: str, programmer: str, hours: int):
        self.description = description
        self.hours = hours
        self.programmer = programmer
        self.workload = hours
        self.id = self.id_new(Task.id)

    def is_finished(self):
        if self.workload == "FINISHED":
            return True
        return False

    def mark_finished(self):
        self.workload = "FINISHED"

    def __str__(self):
        if self.workload == self.hours:
            return f"{self.id}: {self.description} ({self.hours} hours), programmer {self.programmer} NOT FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.hours} hours), programmer {self.programmer} FINISHED"

class OrderBook:
    def __init__(self):
        self.__orders = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.__orders.append(order)

    def all_orders(self):
        return self.__orders

    def programmers(self):
        return list(set(order.programmer for order in self.__orders))

    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self):
        return [order for order in self.__orders if order.workload == "FINISHED"]

    def unfinished_orders(self):
        return [order for order in self.__orders if order.workload != "FINISHED"]

    def status_of_programmer(self, programmer: str):
        fin = []
        unfin = []
        flag = True
        for order in self.__orders:
            if order.programmer == programmer:
                flag = False
                if order.workload == "FINISHED":
                    fin.append(order)
                else:
                    unfin.append(order)
        if flag:
            raise ValueError
        t1 = len(fin)
        t2 = len(unfin)
        t3 = sum([order.hours for order in fin])
        t4 = sum([order.hours for order in unfin])
        return (t1, t2, t3, t4)

if __name__ == "__main__":
    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    t.mark_finished(1)
    for order in t.all_orders():
        print(order)
