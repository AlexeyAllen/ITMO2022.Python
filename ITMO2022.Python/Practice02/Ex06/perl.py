# from Practice02.Ex06.zip_util import read_zip_all
from math import sin, cos, sqrt, atan2, radians

import sys
sys.path.append(r'..\Ex06')
import zip_util

def deg_lat_convert(deg):
    m, s = divmod(abs(deg) * 3600, 60)
    d, m = divmod(m, 60)
    if deg < 0:
        d = -d
    d, m = int(d), int(m)
    hemi = 'N' if d >= 0 else 'S'
    string = f'{d:d}° {m:d}′ {s:.{2:d}f}″ {hemi:1s}'.format(d=abs(d), m=m, s=s, hemi=hemi)
    return string


def deg_long_convert(deg):
    m, s = divmod(abs(deg) * 3600, 60)
    d, m = divmod(m, 60)
    if deg < 0:
        d = -d
    d, m = int(d), int(m)
    hemi = 'E' if d >= 0 else 'W'
    return f'{d:d}° {m:d}′ {s:.{2:d}f}″ {hemi:1s}'.format(d=abs(d), m=m, s=s, hemi=hemi)


def get_city_state(city, state):
    zips = []
    selected_city = ""
    selected_state = ""

    for line in zip_codes:
        if line[3] == city and line[4] == state:
            selected_city = line[3]
            selected_state = line[4]
            zips.append(line[0])

    return f"{selected_city} and {selected_state} : {zips}"


def get_distance(zip1, zip2):
    earth_rad_miles = 3956.0

    lat1, long1, lat2, long2 = 0, 0, 0, 0

    for line in zip_codes:
        if int(line[0]) == int(zip1):
            lat1 = line[1]
            long1 = line[2]
        if int(line[0]) == int(zip2):
            lat2 = line[1]
            long2 = line[2]

    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)
    dlong = long2 - long1
    dlat = lat2 - lat1

    a = abs(sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = earth_rad_miles * c
    return f'{distance:.2f}'

zip_codes = zip_util.read_zip_all()

def main():
    while True:
        input_data = input("Command ('loc', 'zip', 'dist', 'end') =>").lower()

        if input_data == "loc":
            try:
                zip = int(input("Enter a ZIP Code to lookup =>"))
                location_data = zip_codes[zip]
                loc_lat = deg_lat_convert(location_data[1])
                loc_long = deg_long_convert(location_data[2])
                print(f"Zip code {location_data[0]} is in {location_data[3]}, {location_data[4]}, {location_data[5]},"
                      f"coordinates: ({loc_lat} , {loc_long})")
            except:
                print("Invalid or unknown ZIP Code")

        if input_data == "zip":
            try:
                city = input("Enter a city name to lookup =>")
                state = input("Enter a state name to lookup =>")
                print(f"The following ZIP Code(s) found for {get_city_state(city, state)}")
            except:
                print("Invalid or unknown city or state")

        if input_data == "dist":
            try:
                zip1 = input("Enter the first ZIP Code =>")
                zip2 = input("Enter the second ZIP Code =>")
                print(f"The distance between {zip1} and {zip2} is {get_distance(zip1, zip2)} miles")
            except:
                print("Invalid or unknown zip")

        elif (input_data == "end"):
            print("Done")
            break
        else:
            print("Invalid command, ignoring")


if __name__ == "__main__":
    main()
