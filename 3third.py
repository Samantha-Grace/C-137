import requests

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

# create a func and give this a baseurl and pass in the endpoint
def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()

# how many pages are there that I need to loop through
def get_pages(response):
    pages = response['info']['pages']
    return pages
    # or/shortcut
    # return response['info']['pages']

# get totel number of characters and how many episodes they have been in
data = main_request(baseurl, endpoint)
print(get_pages(data))

pages = data['info']['pages']

name = data['results'][0]['name']

episodes = data['results'][0]['episode']


