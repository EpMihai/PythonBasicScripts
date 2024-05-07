import json
import requests

url = "https://swapi.dev/api/people/"
try:
    response = requests.get(url)
except Exception as e:
    print ("Unable to contact API {}".format (e))
    exit

if response.status_code != 200:
    print("Didn't recieve a successful response from api")
else:
    """
    print(response.content.decode())
    people=type (response.content.decode)
    print(people)
    """
    for element in response.json()["results"]:
       print (element)