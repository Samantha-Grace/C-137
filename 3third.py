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

# func to work through the character info on each request and make into a loop
def parse_json(response):
    for item in response['results']:
        print(item['name'], len(item['episode']))
    return




# get totel number of characters and how many episodes they have been in
data = main_request(baseurl, endpoint)
print(get_pages(data))
parse_json(data)


