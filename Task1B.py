from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key


def run():
    # Coordinate at Cambridge City Centre
    p = (52.2053, 0.1218)

    # Empty lists to hold the nearest and furthest 10 stations
    smallest_ten = []
    biggest_ten = []

    # Build a list of stations
    stations = build_station_list()

    # Calculate the distance between the Coordinate p and each station
    distance_list = stations_by_distance(stations, p)

    # Append information to empty list
    for i in range(0, 10):
        smallest_ten.append(distance_list[i])
        biggest_ten.append(distance_list[- 1 - i])

    # Display obtained lists
    print(smallest_ten, sorted_by_key(biggest_ten, 1))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
