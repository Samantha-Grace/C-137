import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

r = requests.get(baseurl + endpoint)

# see what we get back
# print(r.json())

# Do stuff with this response to get what we want
data = r.json()

# save into variable 
pages = data['info']['pages']

