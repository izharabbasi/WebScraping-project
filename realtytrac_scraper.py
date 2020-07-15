import requests
from lxml import html

resp = requests.get(url='https://www.realtytrac.com/mapsearch/ny/new-york-county-foreclosures.html?sortbyfield=featured,desc', headers={
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
})

print(resp)