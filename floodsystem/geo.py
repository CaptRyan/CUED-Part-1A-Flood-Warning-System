# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


# Calculating the distance between the coordinate p and each station
def stations_by_distance(stations, p):
    distance_list = []
    coord_p = p

    # Calculating distance via haversine and store in a list
    for i in stations:
        coord_s = i.coord
        distance = haversine(coord_s, coord_p)
        distance_list.append((i.name, distance))

    # Sort the list from nearest to furthest distances
    distance_list = sorted_by_key(distance_list, 1)

    return distance_list


def stations_within_radius(stations, centre, r):
    within_radius_list = []

    # Fetch the distance from the coordinate to each station
    distance_list = stations_by_distance(stations, centre)
    for i in distance_list:

        # Finding the distance that is within the given radius, adding the name of the station into the list
        if i[1] <= r:
            within_radius_list.append(i[0])

    # Sort the list of names in alphabetical order
    within_radius_list.sort()

    return within_radius_list


def rivers_with_station(stations):
    river_station_list = []
    return river_station_list
