from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


def test_stations_highest_rel_level():
    """Test of calling the function"""

    # Construct a list of stations
    stations = build_station_list()
    N = 6

    stations_highest_rel_level(stations, N)


def test_station_level_over_threashold():
    """Test of returning value for station created for test"""

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (1, 3)
    river = "River X"
    town = "My Town"
    latest_level = 10
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    assert 4.4 < s.relative_water_level() < 4.6
