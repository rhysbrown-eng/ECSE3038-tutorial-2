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

    status_dict = {"device": device["name"]}

    if (device["online"] == True): status_dict["status"] = "online"
    else: status_dict["status"] = "offline"

    status_dict["celsius"] = device["temp"]

    return status_dict


def by_room(devices):
    # return a dictionary of room names to lists of device names

    room_dict = {}
    for device in devices:
        if (not (device["room"] in room_dict)): room_dict["room"] = []

        room_dict["room"].append(device["name"]) 

    return room_dict


