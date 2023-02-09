from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels


def run():

    # Build station list
    stations = build_station_list()
    update_water_levels(stations)

    # Create empty list to hold towns at risk of flooding and flood risk
    towns_with_risk = []

    # Test if relative water level is above threashold, and return risk of flooding
    for i in stations:
        if (i.typical_range_consistent() is True) and (i.relative_water_level() is not None):
            if i.relative_water_level() > 1.5:
                towns_with_risk.append((i.town, "Severe"))
            elif i.relative_water_level() > 1.3:
                towns_with_risk.append((i.town, "High"))
            elif i.relative_water_level() > 1.1:
                towns_with_risk.append((i.town, "Moderate"))
            elif i.relative_water_level() > 1:
                towns_with_risk.append((i.town, "Low"))

    towns_with_risk.sort()
    return towns_with_risk


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    print(run())
