from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    # Build a list of stations
    stations = build_station_list()

    # Saving the list that contains all the name of rivers
    river_list = rivers_with_station(stations)

    # First half of Task1D
    print(f"{len(river_list)} stations. First 10 - {river_list[0:10]}")

    # Second half of Task1D
    river_station = stations_by_river(stations)
    print(river_station["River Aire"])
    print(river_station["River Cam"])
    print(river_station["River Thames"])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
