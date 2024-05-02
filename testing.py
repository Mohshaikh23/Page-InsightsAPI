import requests
import json

url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

params = {
    "url": "https://www.precisevirtualteam.com",
    "strategy":"desktop",
    "key": "AIzaSyDasl6GVbKprqBSWjS43e269-mMg86K5uU",
    "category": ["accessibility","best-practices",
                 "performance","pwa", "seo"]
}

res = requests.get(url, params=params)

with open("response.json", "w") as f:
    json.dump(res.json(), f)