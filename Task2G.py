from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels


def run():

    # Build station list
    stations = build_station_list()
    update_water_levels(stations)

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
                if towns_with_risk[town].values() == "Severe":
                    towns_with_risk[town] = "Severe"
                else:
                    towns_with_risk[town] = "High"
            elif i.relative_water_level() > 1.1:
                if towns_with_risk[town].values() == "Severe":
                    towns_with_risk[town] = "Severe"
                elif towns_with_risk[town].values() == "High":
                    towns_with_risk[town] = "High"
                else:
                    towns_with_risk[town] = "Moderate"
            elif i.relative_water_level() > 1:
                if towns_with_risk[town].values() == "Severe":
                    towns_with_risk[town] = "Severe"
                elif towns_with_risk[town].values() == "High":
                    towns_with_risk[town] = "High"
                elif towns_with_risk[town].values() == "Moderate":
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
    return towns_with_risk, stations[12].town


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    print(run())
