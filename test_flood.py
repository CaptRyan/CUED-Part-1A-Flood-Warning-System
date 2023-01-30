from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def test_stations_highest_rel_level():
    """Test of calling the function"""

    # Construct a list of stations
    stations = build_station_list()
    N = 6

    stations_highest_rel_level(stations, N)
