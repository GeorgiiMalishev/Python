import requests
import json

response = requests.get("https://swapi.dev/api/starships/10/")
ship_data = response.json()
ship_name = ship_data['name']
max_speed = ship_data['max_atmosphering_speed']
ship_class = ship_data['starship_class']
pilot_urls = ship_data['pilots']
pilots_data = []
for url in pilot_urls:
    response = requests.get(url)
    pilot_data = response.json()
    pilots_data.append({
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld_url': pilot_data['homeworld'],
    })
for pilot in pilots_data:
    response = requests.get(pilot['homeworld_url'])
    homeworld_data = response.json()
    pilot['homeworld_name'] = homeworld_data['name']

ship_info = {
    'name': ship_name,
    'max_speed': max_speed,
    'class': ship_class,
    'pilots': pilots_data,
}

print(json.dumps(ship_info, indent=4))

with open('ship_info.json', 'w') as f:
    json.dump(ship_info, f, indent=4)
