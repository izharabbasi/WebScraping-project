import requests
from lxml import html
import csv

def get(l):
    try:
        return l.pop(0)
    except:
        return ''

def write_csv(data):
    headers = ['title','address','price' ,'size','availability','contact']
    with open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(data)



extracted_properties = []
for x in range(1,29):
    resp =requests.get(url=f'https://www.apartments.com/chicago-il/{x}/', headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
    })

    tree = html.fromstring(html=resp.content)

    main = tree.xpath("//div[@id='placardContainer']/ul/li/article")

    for prop in main:
        p={
            'title': get(prop.xpath(".//header[@class='placardHeader']/a/text()")).strip(),
            'address': get(prop.xpath(".//header[@class='placardHeader']/div/text()")),
            'price': get(prop.xpath(".//section[@class='placardContent']/div[2]/div/div[2]/span[1]/text()")),
            'size': get(prop.xpath(".//section[@class='placardContent']/div[2]/div/div[2]/span[2]/text()")),
            'availability': get(prop.xpath(".//section[@class='placardContent']/div[2]/div/div[2]/span[3]/text()")),
            'contact': get(prop.xpath(".//section[@class='placardContent']/div[2]/div/div[3]/div/span/text()"))
        }
        extracted_properties.append(p)

print(len(extracted_properties))
write_csv(extracted_properties)