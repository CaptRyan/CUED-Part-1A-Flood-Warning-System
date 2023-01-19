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
