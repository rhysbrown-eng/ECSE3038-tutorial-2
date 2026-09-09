readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    #print each device's name and temperature

    for device in devices:
        print(f"Device Name: {device["name"]}, Temperature Reading: {device["temp"]}\n")


def average_temp(devices):
    #returns the average temperature

    sum = 0
    i=0

    for device in devices:
        sum += device["temp"]
        i += 1

    return sum/i

def hottest(devices):
    #return the whole dictionary of the hottest device
    max_idx = 0
    i=0

    for device in devices:
        if device["temp"] > devices[max_idx]["temp"]: max_idx = i
        i+=1

    return devices[max_idx]

def to_status(device):
    #take one device, return a new dictionary

    new_dict = {"device": device["name"]}

    if (device["online"] == True): new_dict["status"] = "online"
    else: new_dict["status"] = "offline"

    new_dict["celsius"] = device["temp"]

    return new_dict






