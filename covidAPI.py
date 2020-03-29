import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
x_rapidapi_key = os.getenv("x_rapidapi_key")

def getGlobalData():
    url = "https://covid-19-data.p.rapidapi.com/totals"
    querystring = {"format":"undefined"}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def getCountryData(country):
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"format":"undefined","name":country}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def getCountryCodeData(code):
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"format":"undefined","code":"mx"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def getCountryDataByCode(code):
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"format":"undefined","code":code}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

def getGlobalData193():

    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()


def getCountryData193(country):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":country}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': x_rapidapi_key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()
