#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""Get the events of GDG Granada from Meetup and convert them to markdown."""

from os import environ
from json import loads
from tomd import convert
from requests import get

url = "https://api.meetup.com/GDG_Granada/events"
apiKey = environ["MEETUPAPI"]
params = {'city': "Granada", 'key': apiKey}
response = get(url, params=params)
responseString = response.text
data = loads(responseString)

for event in data:
    if event["visibility"] == "public":
        print("## [ " + event["name"] + "](" + event["link"] + ")")
        print()
        print("En: [" + event["venue"]["name"] +
              "](https://www.google.es/maps/@" + str(event["venue"]["lat"]) +
              "," + str(event["venue"]["lon"]) + ",18z)")
        print(convert(event["description"]))
        print("### [ Apuntarse al evento ](" + event["link"] + ")")
        print()
        print()
