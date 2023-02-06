from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threashold
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key


def run():
    stations = build_station_list()
    update_water_levels(stations)

    return_list = stations_level_over_threashold(stations, 0.8)
    return_list = sorted_by_key(return_list, 1, True)

    for i in return_list:
        print(i[0], i[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
