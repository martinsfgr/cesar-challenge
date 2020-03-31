import requests
import json

url = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=6f79cbdd3978211426d28849c5760bbb48337f26")
json_data = url.json()

with open('answer.json', 'w') as f:
    json.dump(json_data, f)

