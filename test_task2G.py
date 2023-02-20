from floodsystem.stationdata import MonitoringStation


def test_Task2G():
    """Test of returning value for station created for test"""

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (1, 3)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 3.1

    # Create another station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 2"
    coord = (-2.0, 4.0)
    trange = (1, 3)
    river = "River X"
    town = "My Town"
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    t.latest_level = 10
