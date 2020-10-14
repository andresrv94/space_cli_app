
import requests, json
from datetime import datetime

def get_amount_astronauts():
    response = requests.get("http://api.open-notify.org/astros.json")
    print("#"*40)
    if response.status_code == 200:
        
        print("Request succesfull!")
        print("Currently, there are "+str(response.json()['number'])+" people in ISS")
        for i in response.json()['people']:
            print(i['name'])
    else:
        print("Error requesting data from API. Status code: "+str(response.status_code))

def get_iss_location():
    print("#"*40)
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        iss_latitude=response.json()['iss_position']['latitude']
        iss_longitude=response.json()['iss_position']['longitude']
        req_timestamp=response.json()['timestamp']
        ts=datetime.utcfromtimestamp(req_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print("Date/time(UTC): "+ts)
        print("The current ISS position is [latidude/longitude]: "+iss_latitude+";"+iss_longitude)
        print("You can check the place at the following link: http://www.google.com/maps/place/"+str(iss_latitude)+","+str(iss_longitude))
    
    else:
        print("Error requesting data from API. Status code: "+str(response.status_code))

def get_next_pass():
    print("#"*40)
    print("Please enter the latitude of the place:")
    lat=input()
    print("Please enter the longitude of the place:")
    lon=input()
    response = requests.get("http://api.open-notify.org/iss-pass.json?lat="+lat+"&lon="+lon+"&n=1")
    if response.status_code == 200:
        t_next_pass=response.json()['response'][0]['risetime']
        t_next_pass_utc=datetime.utcfromtimestamp(t_next_pass).strftime('%Y-%m-%d %H:%M:%S')
        print("The next pass will be at: "+t_next_pass_utc)
    else:
        print("Error requesting data from API. Status code: "+str(response.status_code))

def print_intro():
    print("#"*40)
    print("Welcome to this test. Using this app you can query info about the ISS in real time.")
    print("#"*40)
    print("Options available:")
    print("[1] Get how many astronauts are in space now")
    print("[2] Get the ISS current location") #Aca podemos referenciarla a un mapa de alguna forma, capaz con Gmaps
    print("[3] See when the ISS is going to pass entering a specific place")