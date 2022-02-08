from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

def run():
    #Build list of stations
    stations = build_station_list()
    #adding the conditions
    coordinate = (52.2053, 0.1218)
    radius = 10
    #using function in geo
    listOfStationsInRadius = stations_within_radius(stations,coordinate,radius)

    print("Stations within a 10km radius of the city centre")
    print(listOfStationsInRadius)


if __name__ == "__main__":
       print("*** Task 1B: CUED Part IA Flood Warning System ***")
       run()


