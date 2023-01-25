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
        distance_list.append((i.name, i.town, distance))

    # Sort the list from nearest to furthest distances
    distance_list = sorted_by_key(distance_list, 2)

    return distance_list


def stations_within_radius(stations, centre, r):
    within_radius_list = []

    # Fetch the distance from the coordinate to each station
    distance_list = stations_by_distance(stations, centre)
    for i in distance_list:

        # Finding the distance that is within the given radius, adding the name of the station into the list
        if i[2] <= r:
            within_radius_list.append(i[0])

    # Sort the list of names in alphabetical order
    within_radius_list.sort()

    return within_radius_list


def rivers_with_station(stations):
    river_names = []
    river_list = []

    # Storing all the names of rivers (contains repeating value)
    for i in stations:
        river_names.append(i.river)

    # Eliminate repeating river names
    river_list = set(river_names)
    river_list = list(river_list)

    # Sort the name of the rivers in alphabetical order
    river_list.sort()

    return river_list


def stations_by_river(stations):
    # Using pre-constructed function
    river_list = rivers_with_station(stations)
    river_station_dictionary = {}

    # Set-up essential data structure for storing information in the later part of the function
    for i in river_list:
        river_station_dictionary[i] = []

    # Storing the name of the stations under index(name of river) in the dictionary
    for i in river_list:
        for j in stations:
            if i == j.river:
                river_station_dictionary[i].append(j.name)

    # Sort the list inside the dictionary which contains names of stations
    for i in river_station_dictionary.items():
        i[1].sort()

    return river_station_dictionary


def rivers_by_station_number(stations, N):
    # Return the N rivers with the greatest number of monitoring stations.
    # Will return a tuple (river name, number of stations) depending on the input value of N

    #Setting up variables for later parts of the function
    number_of_stations = []
    top_N_stations = []
    list_complete = False
    
    #Create list of ("river name", "number of stations") tupels
    river_dict = stations_by_river(stations)
    for i in range(len(list(river_dict.keys()))):
        number_of_stations.append((list(river_dict.keys())[i], len(list(river_dict.items())[i][1])))
        number_of_stations = sorted_by_key(number_of_stations, 1, True)

    #Selects N rivers with the most stations
    top_N_stations = number_of_stations[:N]

    #Creates list containing the number of station on each river in numerical order
    stations = [tup[1] for tup in number_of_stations]
    
    #Adds rivers to the end of the list if the river has the same number of stations as the Nth river
    while list_complete == False:
        if stations[N-1] == stations[N]:
            top_N_stations.append(number_of_stations[N])
            N = N+1
        else:
            
            list_complete = True
    

    return top_N_stations
    
