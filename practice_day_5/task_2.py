import urllib.request, json

def get_data_from_url(url):
    response = urllib.request.urlopen(url)
    return json.loads(response.read())

def parse_heroes(data):
    return [item['name'] for item in data]

def find_weapon(data):
    return [{item['name']: item['weapon']} for item in data if item['weapon']]

data = get_data_from_url("https://lego-super-heroes.herokuapp.com/")

print(parse_heroes(data))
print(find_weapon(data))