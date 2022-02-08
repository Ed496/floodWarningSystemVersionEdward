# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
try:
    from .utils import sorted_by_key  # noqa
except ImportError:
    from utils import sorted_by_key

#function to sort a list of stations by their distance away from a point p

def stations_by_distance(stations, p):
    '''returns a list of stations sorted by how far away they are from the point p'''
    #creating a list
    listStations = []

    #inserting in to the list the station names, towns, and distance away from a point p
    for i in stations:
        listStations.append((i.name, i.town, haversine(i.coord, p)))

    #sorting the list by their distance away from a point p
    sortedList = sorted_by_key(listStations, 2)

    return(sortedList)



def stations_within_radius(stations, centre, r):
    '''returns a list of stations within a radius of a point, sorted alphabetically'''
    #creating a list
    stationsInRadius = []
    #finding the radius of each station from the centre
    for i in stations:
        radius = haversine(i.coord, centre)
    #insterting the stations with radius smaller than r in to the list
        if radius <= r:
            stationsInRadius.append(i.name)

    sortedList2 = sorted_by_key(stationsInRadius, 0)

    return(sortedList2)