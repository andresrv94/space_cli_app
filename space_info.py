import requests, json

def print_intro():
    print("#"*40)
    print("Welcome to this test. Using this app you can query info about the ISS in real time.")
    print("#"*40)
    print("Options available:")
    print("[1] Get how many astronauts are in space now")
    print("[2] Get the ISS current location") #Aca podemos referenciarla a un mapa de alguna forma, capaz con Gmaps
    print("[3] See when the ISS is going to pass entering a specific place")

def main_function():
    selection=input()
    if selection == "1":
        get_amount_astronauts()
    elif selection == "2":
        print("Second choice")
    elif selection == "3":
        print("Third choice")
    else:
        print("You entered a non-valid value. Please run the app again.")

def get_amount_astronauts():
    response = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code == 200:
        print("Request succesfull!")
        print("Currently, there are "+str(response.json()['number'])+" people in ISS")
    else:
        print("Error requesting data from API. Status code: "+str(response.status_code))

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


print_intro()
main_function()