# coding: utf-8
import requests
import json
from covidAPI import getCountryDataByCode
def reverseGeocode(lat, long):
    url = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={long}&localityLanguage=en"
    response = requests.get(url)
    return response.json()
    
