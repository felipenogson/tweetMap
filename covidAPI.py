import requests

def getGlobalData():
    url = "https://covid-19-data.p.rapidapi.com/totals"
    querystring = {"format":"undefined"}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "5b1c9c9c19mshbec01bd7a4611b9p1fdfddjsn25d9cc52e373"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def getCountryData(country):
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"format":"undefined","name":country}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "5b1c9c9c19mshbec01bd7a4611b9p1fdfddjsn25d9cc52e373"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def getCountryCodeData(code):
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"format":"undefined","code":"mx"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "5b1c9c9c19mshbec01bd7a4611b9p1fdfddjsn25d9cc52e373"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()