import requests

url ="http://localhost:8000/tacos"
headers ={"content-typer":"application/json"}

response =requests.get(url)
print(response.json())

mi_taco={
    "tamaño":"mediano",
    "masa":"maiz",
    "ingredientes":["Carnitas","queso"]
}
response=requests.post(url, json=mi_taco,headers=headers)
print(response.json)

response =requests.get(url)
print(response.json())

edit_taco= {
    "tamaño": "Mediano",
    "masa": "Gruesa",
    "ingredientes": ["Pepperoni", "Queso"]
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

response = requests.get(url)
print(response.json())

response = requests.delete(url + "/1")
print(response.json())

response = requests.get(url)
print(response.json())