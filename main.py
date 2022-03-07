import requests

r = requests.get("https://www.balldontlie.io/api/v1/players/179")
print(r.json())