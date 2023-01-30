import matplotlib.pyplot as plt
import matplotlib
from datetime import timedelta
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels


def plot_water_levels(station, dates=None, levels=None, dt=10):
    # Creating empty lists for dates and levels
    dates_self = dates
    levels_self = levels

    # Fetching dates and levels for specific station
    if station.measure_id[0:4] != "http":
        pass
    else:
        dates_self, levels_self = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

    # Plot
    plt.plot(dates_self, levels_self)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station {station.name}")

    # Plot of typical minimum and typical maximum, adding legend for clarity
    plt.plot(dates_self, [station.typical_range[0]] * len(dates_self), label="Min")
    plt.plot(dates_self, [station.typical_range[1]] * len(dates_self), label="Max")
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates=None, levels=None, p=4, dt=2):
    # Creating empty lists for dates and levels
    dates_self = dates
    levels_self = levels

    # Fetching dates and levels for specific station
    if station.measure_id[0:4] != "http":
        pass
    else:
        dates_self, levels_self = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

    x = matplotlib.dates.date2num(dates_self)
    poly, d0 = polyfit(x, levels_self, p)
    y = poly(x - d0)
    plt.plot(dates_self, y, label="Power Fit")
    plt.plot(dates_self, levels_self, label="Original")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station {station.name}")

    # Plot of typical minimum and typical maximum, adding legend for clarity
    plt.plot(dates_self, [station.typical_range[0]] * len(dates_self), label="Min")
    plt.plot(dates_self, [station.typical_range[1]] * len(dates_self), label="Max")
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
