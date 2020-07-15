import requests
from lxml import html
import csv
from urllib.parse import urljoin

def get(l):
    try:
        return l.pop(0)
    except:
        return ''

def write_csv(data):
    headers = ['selling_type', 'address', 'city' , 'region', 'postal_code', 'price']
    with open("data.csv", 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(data)


extracted_properties = []
def scraper(url):
    resp = requests.get(url=url, headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
    })

    tree = html.fromstring(html=resp.content)

    main = tree.xpath("//section/div[@id='housesList']/div[@itemtype='http://schema.org/SingleFamilyResidence']")

    for prop in main:
        p ={
            'selling_type': prop.xpath(".//div[@class='content']/div/a/span/text()"),
            'address': prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[1]/text()"),
            'city': prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[2]/text()"),
            'region':prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[3]/text()"),
            'postal_code':prop.xpath(".//div[@class='content']/div[2]/div/div/a/strong/span[4]/text()"),
            'price': prop.xpath(".//div[@class='content']/div[3]/dl/dd[1]/text()"),
            
        }
        extracted_properties.append(p)
    next_page = tree.xpath("//a[@class='next']/@href")
    if len(next_page) !=0:
        next_page_url = urljoin(base=url, url=next_page[0])
        scraper(url=next_page_url)

scraper(url='https://www.realtytrac.com/mapsearch/ny/new-york-county-foreclosures.html?sortbyfield=featured,desc')
    
print(len(extracted_properties))
write_csv(extracted_properties)