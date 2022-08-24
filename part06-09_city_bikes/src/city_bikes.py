# tee ratkaisu tänne
# Write your solution here
from math import sqrt 

def get_station_data(filename: str):
    with open(filename) as file:
        dct = {}
        for line in file:
            line = line.split(";")
            if line[0] == "Longitude":
                continue
            dct[line[3]] = (float(line[0]), float(line[1]))
    return dct

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_dist = 0
    answ_list = ["", ""]
    for station1 in stations:
        for station2 in stations:
            dist = distance(stations, station1, station2)
            if dist > max_dist:
                max_dist = dist
                answ_list[0] = station1
                answ_list[1] = station2
    return (answ_list[0], answ_list[1], max_dist)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
