import json, requests
url = requests.get("https://thingproxy.freeboard.io/fetch/https://api.scratch.mit.edu/users/griffpatch/messages/count")
text = url.text
data = json.loads(text)
print(data['count'])
