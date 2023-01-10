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
# After info, we have results, we want to check out the first item in that list
# print(data['results'][0])

# get name (accessing diff parts of the json data)
name = (data['results'][0]['name'])

episodes = (data['results'][0]['episode'])

print(episodes)

# How many episodes is this character in?
# Find length of episode/how many there are
print(len(episodes))  # 51


