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

# What parts of other info do we want - check the docs
# After info, we have results, lets check out the first item in that list
print(data['results'][0])