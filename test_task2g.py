from floodsystem.stationdata import MonitoringStation


def test_Task2G():
    """Test of returning correct flood risk for town with two stations"""

    def create_test_stations():
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
        t.latest_level = 8

        created_stations = {s, t}

        return created_stations

    # Build station list
    stations = create_test_stations()

    def add_to_dict(town):

        # Check if town is already in list
        if town not in towns_with_risk.keys():
            if i.relative_water_level() > 1.5:
                towns_with_risk[town] = "Severe"
            elif i.relative_water_level() > 1.3:
                towns_with_risk[town] = "High"
            elif i.relative_water_level() > 1.1:
                towns_with_risk[town] = "Moderate"
            elif i.relative_water_level() > 1:
                towns_with_risk[town] = "Low"
        elif town in towns_with_risk.keys():
            if i.relative_water_level() > 1.5:
                towns_with_risk[town] = "Severe"
            elif i.relative_water_level() > 1.3:
                if towns_with_risk[town] == "Severe":
                    towns_with_risk[town] = "Severe"
                else:
                    towns_with_risk[town] = "High"
            elif i.relative_water_level() > 1.1:
                if towns_with_risk[town] == "Severe":
                    towns_with_risk[town] = "Severe"
                elif towns_with_risk[town] == "High":
                    towns_with_risk[town] = "High"
                else:
                    towns_with_risk[town] = "Moderate"
            elif i.relative_water_level() > 1:
                if towns_with_risk[town] == "Severe":
                    towns_with_risk[town] = "Severe"
                elif towns_with_risk[town] == "High":
                    towns_with_risk[town] = "High"
                elif towns_with_risk[town] == "Moderate":
                    towns_with_risk[town] = "Moderate"
                else:
                    towns_with_risk[town] = "Low"

    # Create empty list to hold towns at risk of flooding and flood risk
    towns_with_risk = {}

    # Test if relative water level is above threashold,
    # and return risk of flooding
    for i in stations:
        if (i.typical_range_consistent() is True) and (i.relative_water_level() is not None):
            add_to_dict(i.town)

    # towns_with_risk.sort()
    assert towns_with_risk == {'My Town': 'Severe'}
