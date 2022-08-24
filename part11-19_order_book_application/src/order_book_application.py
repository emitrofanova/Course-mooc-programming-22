# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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
        self._orders = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self._orders.append(order)

    def all_orders(self):
        return self._orders

    def programmers(self):
        return list(set(order.programmer for order in self._orders))

    def mark_finished(self, id: int):
        for order in self._orders:
            if order.id == id:
                order.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self):
        return [order for order in self._orders if order.workload == "FINISHED"]

    def unfinished_orders(self):
        return [order for order in self._orders if order.workload != "FINISHED"]

    def status_of_programmer(self, programmer: str):
        fin = []
        unfin = []
        flag = True
        for order in self._orders:
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




class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ")
        programmer = programmer_workload.split()[0]
        workload = int(programmer_workload.split()[1])
        self.__orderbook.add_order(description, programmer, workload)
        print("added!")

    def finished_tasks(self):
        if self.__orderbook.finished_orders() == []:
            print("no finished tasks")
            return
        for order in self.__orderbook.finished_orders():
            print(order)

    def unfinished_tasks(self):
        if self.__orderbook.unfinished_orders() == []:
            print("no unfinished tasks")
            return
        for order in self.__orderbook.unfinished_orders():
            print(order)

    def mark_fin(self):
        id = int(input("id: "))
        self.__orderbook.mark_finished(id)
        print("marked as finished")

    def programmers(self):
        for item in self.__orderbook.programmers():
            print(item)
    
    def status(self):
        programmer = input("programmer: ")
        stat = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {stat[0]} not finished {stat[1]}, hours: done {stat[2]} scheduled {stat[3]}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                try:
                    self.add_order()
                except:
                    print("erroneous input")
                    continue
            elif command == "2":
                try:
                    self.finished_tasks()
                except:
                    print("erroneous input")
                    continue
            elif command == "3":
                try:
                    self.unfinished_tasks()
                except:
                    print("erroneous input")
                    continue
            elif command == "4":
                try:
                    self.mark_fin()
                except:
                    print("erroneous input")
                    continue
            elif command == "5":
                try:
                    self.programmers()
                except:
                    print("erroneous input")
                    continue
            elif command == "6":
                try:
                    self.status()
                except:
                    print("erroneous input")
                    continue
            else:
                self.help()

# when testing, no code should be outside application except the following:
application = OrderBookApplication()
application.execute()
