import requests
import json

url = "https://icanhazdadjoke.com/"
res = requests.get(url, headers={"Accept": "text/plain"})

print(res.text)
