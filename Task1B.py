from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key


def run():
    p = (52.2053, 0.1218)
    smallest_ten = []
    biggest_ten = []

    stations = build_station_list()
    distance_list = stations_by_distance(stations, p)
    for i in range(0, 10):
        smallest_ten.append(distance_list[i])
        biggest_ten.append(distance_list[- 1 - i])
    print(smallest_ten, sorted_by_key(biggest_ten, 1, False))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
