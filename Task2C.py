from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels


def run():
    # Build station list
    stations = build_station_list()
    update_water_levels(stations)

    # Calling required function
    returned_list = stations_highest_rel_level(stations, 10)
    for i in returned_list:
        print(f"{i.name} {i.relative_water_level()}")


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
