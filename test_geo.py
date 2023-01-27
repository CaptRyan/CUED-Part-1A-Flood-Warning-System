"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number


def test_stations_by_distance():
    """Test of calculating distance and sorting"""

    # Self-defined coordinate
    p = (30.2986, 33.5382)

    # Construct a list of stations
    stations = build_station_list()

    # Calling the function
    list_stations_by_distance = stations_by_distance(stations, p)

    # Verify the result
    assert (list_stations_by_distance[0][2] - 3522.703867078437) < 0.00001


def test_stations_within_radius():
    """Test of calculation"""

    # Centre and radius definition
    centre = (52.2053, 0.1218)

    # Construct a list of stations
    stations = build_station_list()
    r = 5

    # Calling the function
    assert len(stations_within_radius(stations, centre, r)) == 3


def test_rivers_with_station():
    """Test of calling the function"""

    # Construct a list of stations
    stations = build_station_list()

    rivers_with_station(stations)


def test_rivers_by_station_number():
    """Test of calling the function"""

    # Construct a list of stations
    stations = build_station_list()
    N = 9

    rivers_by_station_number(stations, N)
