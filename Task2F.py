from floodsystem.plot import plot_water_level_with_fit
# from datetime import datetime
# from floodsystem.stationdata import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key


def run():
    # Initialization of variables that are needed afterwards
    stations = build_station_list()
    update_water_levels(stations)
    stations_relative_water_level = []

    for i in stations:
        if i.typical_range_consistent():
            # Ignoring None Type latest_level
            if i.latest_level is None:
                pass
            else:
                stations_relative_water_level.append((i, i.relative_water_level()))

    # Sorting stations by their relative water level
    stations_relative_water_level = sorted_by_key(stations_relative_water_level, 1, True)

    # Obtaining the list that contains the largest five of the relative water level differences
    largest_relative_level = stations_relative_water_level[0:5]
    for i in largest_relative_level:
        plot_water_level_with_fit(i[0], p=4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
