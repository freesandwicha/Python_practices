# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 1/9/2023 11:05 am

# Calculate the direct distance between two addresses.
# Main function: Set a base address(Home address), then let users input the another address they want to calculate.

from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude
   #it will return a tuple (self.latitude,self.longitude).


def get_coordinates(address: str) -> Coordinates | None:
    geolocator = Nominatim(user_agent='distance_calculate')
    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)
#      it returns an instance of Coordinates containing the latitude and longitude of that address


def calculate_distance_km(home_address: Coordinates, target_address: Coordinates) -> float | None:
    if home_address and target_address:
        distance: float = geodesic(home_address.coordinates(), target_address.coordinates()).kilometers
        return distance


def get_distance(home_address: str, target_address: str) -> float|None:
    home_coordinates: Coordinates = get_coordinates(home_address)
    target_coordinates: Coordinates = get_coordinates(target_address)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'The distance  between \'{home_address}\' to \'{ target_address}\' is {distance:.2f} kms')
        return distance
    else:
        print('Fail to calculate the distance...')


def main():
    home_address: str = 'Cooper St, Cessnock NSW 2325'
    print(f'Home address : {home_address}')
    target_address: str = input('Your address: ')
    get_distance(home_address, target_address)


if __name__ == '__main__':
    main()
