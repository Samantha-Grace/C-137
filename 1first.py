import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

r = requests.get(baseurl + endpoint)

# see what we get back
# print(r.json())

# Do stuff with this response to get what we want
data = r.json()

# access the keys with square brackets
print(data['info'])

