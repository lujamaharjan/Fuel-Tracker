import urllib.request
import json

# this function return the entire json data
def fetchJsonData(url):

    # requesting internet to open the given url and
    # fetch json data and store in variable json_obj
    json_obj = urllib.request.urlopen(url)

    # fetched data is serialized and in unicode form
    # so, to deserializeing data we use json.load() method
    dataList = json.load(json_obj)

    # so, our data is list of dictionary so we return
    # list of dictionary
    return(dataList)
