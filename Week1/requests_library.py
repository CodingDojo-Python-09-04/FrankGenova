"""Coding Dojo - Python Fundamentals - Optional Assignment: The Requests Library

Build a simple program that makes use of the requests module.
In addition to including a lot of great features in the language itself,
there are many modules available for install via pip that are a lot of fun to work with.
We talked a little about pip before,
so you should have the basic idea that pip exists
so that developers can use code other people have written.

One of those code libraries is called requests.
It allows you to make HTTP requests from a python file and get back a useful response.
This library is a simple way to make requests to and get responses from a server
without having to set one up yourself.
This might remind you a little of using AJAX to interact with API's
like you did in web fundamentals.
Give it a try and get creative with the data you try to get back.
You'll have a much easier time if you install a virtual environment.

"""

import os
import requests
import json


def clear():
    """Clear the screen"""
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def main():
    keyAPI = "849e3a48b582285b1199513c5c6734b1"
    payload={"id":"524901","APPID":keyAPI, "zip":"22209,us"}
    weatherAPI = "http://api.openweathermap.org/data/2.5/weather"
    r = requests.get(weatherAPI, params=payload)
    json_data = json.loads(r.text)
    clear()
    print("="*80)
    print("\nThe URL:\n{}\n".format(r.url))
    print("="*80)
    print("\nThe text:\n{}\n".format(r.text))
    print("="*80)
    print("\nThe JSON:\n{}\n".format(json_data))
    print("="*80)
    print("\nIterate json_data keys:\n")
    for key in json_data.keys():
        print(key)
    print("="*80)
    temp = json_data["main"]["temp"]
    print("\ntemp:\n{}\n".format(temp))
    print("="*80)    
        
    
if __name__ == '__main__':
    main() 