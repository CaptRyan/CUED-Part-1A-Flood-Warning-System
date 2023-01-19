"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    """Test of calculating distance and sorting"""

    # Self-defined coordinate
    p = (30.2986, 33.5382)

    # Construct a list of stations
    stations = build_station_list()

    # Calling the function
    list_stations_by_distance = stations_by_distance(stations, p)

    # Verify the result
    assert (list_stations_by_distance[0][1] - 3522.703867078437) < 0.00001
