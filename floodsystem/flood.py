from floodsystem.utils import sorted_by_key


def stations_level_over_threashold(stations, tol):

    stations_over_threashold = []

    for i in stations:
        if (i.latest_level is not None and i.relative_water_level() is not None) and i.relative_water_level() > tol:
            stations_over_threashold.append((i.name, i.relative_water_level()))
    return stations_over_threashold


def stations_highest_rel_level(stations, N):
    stations_relative_water_level = []
    station_list = []
    for i in stations:
        if i.typical_range_consistent():
            # Ignoring None Type latest_level
            if i.latest_level is None:
                pass
            else:
                stations_relative_water_level.append((i, i.relative_water_level()))

    # Sorting stations by their relative water level
    stations_relative_water_level = sorted_by_key(stations_relative_water_level, 1, True)
    for i in stations_relative_water_level:
        station_list.append(i[0])

    # Obtaining the list that contains the largest N of the relative water level differences
    return station_list[0:N]
