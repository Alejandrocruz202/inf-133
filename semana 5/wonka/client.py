import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate_data = {
    "chocolate_type": "tableta",
    "peso": "120g",
    "sabor": "cholate",
    "relleno":None
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "bombones",
    "peso": "50g",
    "sabor": "blanco",
    "relleno":"chuño"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{vehicle_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": "200g"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print(f"chocolate actualizado:{chocolate_id_to_update}", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# DELETE /deliveries/{vehicle_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print(f"chocolate {chocolate_id_to_delete} eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())