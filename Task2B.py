from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threashold


def run():
    stations = build_station_list()

    print(stations_level_over_threashold(stations, 5))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
