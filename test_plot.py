from datetime import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import MonitoringStation


def test_plot_water_levels():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1), datetime(2017, 1, 2),
         datetime(2017, 1, 3), datetime(2017, 1, 4), datetime(2017, 1, 5)]
    level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    # Test of plotting the graph
    plot_water_levels(s, t, level)
