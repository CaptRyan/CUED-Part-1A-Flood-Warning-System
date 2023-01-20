from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    # Coordinate at Cambridge City Centre
    p = (52.2053, 0.1218)

    # Build a list of stations
    stations = build_station_list()

    # Calling stations_within_radius function
    list_return = stations_within_radius(stations, p, 10)
    print(list_return)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
