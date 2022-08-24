# Write your solution here
import json
class HockeyBook:
    def __init__(self):
        self._statistics = []

    def add_data(self, all_data):
        self._statistics = all_data

    def search_name(self, name):
        player = [player for player in self._statistics if player["name"] == name]
        player = player[0]
        self.print_f(player)
    
    def print_f(self, player):
        print(f"{player['name']:20} {player['team']:4} {player['goals']:2} + {player['assists']:2} = {(player['goals'] + player['assists']):3}")
    
    def teams(self):
        teams_list = set(player["team"] for player in self._statistics)
        for team in sorted(teams_list):
            print(team)

    def countries(self):
        countries_list = set(player["nationality"] for player in self._statistics)
        for country in sorted(countries_list):
            print(country)
        
    def in_team(self, team):
        players = [player for player in self._statistics if player["team"] == team]
        players = sorted(players, key=lambda player : player["goals"] + player["assists"], reverse = True)
        for player in players:
            self.print_f(player)

    def from_country(self, country):
        players = [player for player in self._statistics if player["nationality"] == country]
        players = sorted(players, key=lambda player : player["goals"] + player["assists"], reverse = True)
        for player in players:
            self.print_f(player)

    def points(self, num):
        players = sorted(self._statistics, key=lambda player : player["goals"], reverse = True)
        players = sorted(players, key=lambda player : player["goals"] + player["assists"], reverse = True)
        for player in players[0:num]:
            self.print_f(player)

    def goals(self, num):
        players = sorted(self._statistics, key=lambda player : player["games"])
        players = sorted(players, key=lambda player : player["goals"], reverse = True)
        for player in players[0:num]:
            self.print_f(player)


class HockeyApplication:
    def __init__(self):
        self.__hockeybook = HockeyBook()

    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def file_read(self, file_name):
        with open(file_name) as f:
            data = f.read()
        all_data = json.loads(data)
        print(f"read the data of {len(all_data)} players")
        self.__hockeybook.add_data(all_data)

    def search_name(self):
        name = input("name: ")
        self.__hockeybook.search_name(name) 
    
    def teams(self):
        self.__hockeybook.teams()

    def countries(self):
        self.__hockeybook.countries()
    
    def in_team(self):
        team = input("team: ")
        self.__hockeybook.in_team(team)

    def from_country(self):
        country = input("country: ")
        self.__hockeybook.from_country(country)

    def points(self):
        num = int(input("how many: "))
        self.__hockeybook.points(num)
    
    def goals(self):
        num = int(input("how many: "))
        self.__hockeybook.goals(num)

    def execute(self):
        file_name = input("file name: ")
        self.file_read(file_name)
        #self.file_read("partial.json")
        print()
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                try:
                    self.search_name()
                except:
                    print("erroneous input")
                    continue
            elif command == "2":
                try:
                    self.teams()
                except:
                    print("erroneous input")
                    continue
            elif command == "3":
                try:
                    self.countries()
                except:
                    print("erroneous input")
                    continue
            elif command == "4":
                try:
                    self.in_team()
                except:
                    print("erroneous input")
                    continue
            elif command == "5":
                try:
                    self.from_country()
                except:
                    print("erroneous input")
                    continue
            elif command == "6":
                try:
                    self.points()
                except:
                    print("erroneous input")
                    continue
            elif command == "7":
                try:
                    self.goals()
                except:
                    print("erroneous input")
                    continue
            else:
                self.help()

# when testing, no code should be outside application except the following:
application = HockeyApplication()
application.execute()
