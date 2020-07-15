import requests
from lxml import html

extracted_properties = []

resp = requests.get(url='https://www.realtytrac.com/mapsearch/ny/new-york-county-foreclosures.html?sortbyfield=featured,desc', headers={
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
})

tree = html.fromstring(html=resp.content)

main = tree.xpath("//section/div[@id='housesList']/div")

for prop in main:
    p ={
        'selling_type': prop.xpath(".//div[@class='content']/div/a/span/text()"),
        'address': prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[1]/text()"),
        'city': prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[2]/text()"),
        'region':prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[3]/text()"),
        'postal_code':prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[4]/text()"),
        'price': prop.xpath(".//div[@class='content']/div[3]/dl/dd[1]/text()"),
        'auction_date': prop.xpath(".//div[@class='content']/div[3]/dl/dd[2]/a/text()"),
    }
    extracted_properties.append(p)

print(len(extracted_properties))