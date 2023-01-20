from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    # Build a list of stations
    stations = build_station_list()
    stations_number = rivers_by_station_number(stations, 0)
    print(stations_number)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()