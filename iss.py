#!/usr/bin/env python

__author__ = """
stephguirand
Help from demo, lessons and activities, youtube videos in canvas and
own search on youtube,
stack overflow, Tutors, Facilitators and talking about assignment
in study group.
"""

import requests
import turtle
import time
import json
# import urllib.request


def list_of_astronauts():

    # A first JSON request to retrieve the name of all the astronauts currently in space.
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    result = json.loads(response.text)
    print("There are currently " +
          str(result["number"]) + " astronauts in space:")
    print("")

    people = result["people"]

    for p in people:
        print(p["name"] + " on board of " + p["craft"])


def iss_location():
    # Display information on world map using Python Turtle
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    # Load the world map picture
    screen.bgpic("map.gif")

    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(45)
    iss.penup()
    indy_location()

    while True:
        # A JSON request to retrieve the current longitude and latitude of the IIS space station (real time)
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        result = json.loads(response.text)

        # Let's extract the required information
        location = result["iss_position"]
        lat = float(location["latitude"])
        lon = float(location["longitude"])

        # Output informationon screen
        print("\nLatitude: " + str(lat))
        print("Longitude: " + str(lon))

        # Plot the ISS on the map
        iss.goto(lon, lat)
        # refresh position every 5 seconds
        time.sleep(5)


def indy_location():
    in_loc = turtle.Turtle()
    in_loc.shape("circle")
    in_loc.turtlesize(.5, .5, .5)
    in_loc.color("green")
    in_loc.penup()
    in_loc.goto(-86.159536, 39.778117)
    payload = {"lat": 39.778117, "lon": -86.159536}
    response = requests.get(
        "http://api.open-notify.org/iss-pass.json", params=payload)
    result = json.loads(response.text)
    next_time = time.ctime(result["response"][0]["risetime"])
    in_loc.write(next_time)


def main():
    list_of_astronauts()
    iss_location()


if __name__ == '__main__':
    main()
