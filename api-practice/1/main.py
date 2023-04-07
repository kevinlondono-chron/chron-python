import requests

BASE_ENDPOINT = "https://rickandmortyapi.com/api/character"
headers = {
    "api-key": "password" # ENV Var
}

data = requests.get(url=BASE_ENDPOINT, headers=headers)

if data.status_code == 200:
    for char in data.json()["results"]:
        print(char["name"])
else:
    data.raise_for_status()


# Eaxmple to Create a Character #
""" data = {"name": "chron", "status": "alive",}
response = requests.post(url=BASE_ENDPOINT, data=data)
print(response) 
 """




