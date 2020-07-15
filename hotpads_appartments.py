import requests
from lxml import html
from urllib.parse import urljoin
import csv

def get(l):
    try:
        return l.pop(0)
    except:
        return ""

def write_csv(data):
    headers = ['price','size','description' ,'address','type']
    with open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(data)

extracted_data = []
for x in range(1,41):
    resp = requests.get(url=f'https://hotpads.com/new-york-ny/apartments-for-rent?page={x}', headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64',
        'Cookie': 'pis=3; ut=BDm0_ExtGpMc6N7yQZP5zCv6nZCuZbUy77Wp8FZrLEY; SESSION_TOKEN=gUj2YzVvVu6BFD849RxRNezmN1iBSW0wi0qUJFEW5GQ; _ga=GA1.2.921165282.1594808978; _gid=GA1.2.1063061952.1594808978; _pxvid=15c437b0-c686-11ea-b6cf-0242ac120008; _gcl_au=1.1.1732515764.1594808981; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jul+15+2020+18%3A09%3A16+GMT%2B0500+(Pakistan+Standard+Time)&version=5.9.0&landingPath=NotLandingPage&groups=1%3A1%2C0_172180%3A1%2C0_248632%3A1%2C0_172218%3A1%2C0_172151%3A1%2C0_172362%3A1%2C3%3A1%2C0_172152%3A1%2C0_172351%3A1%2C4%3A1%2C0_172338%3A1%2C0_172360%3A1%2C0_172153%3A1%2C0_172154%3A1%2C0_172343%3A1%2C0_177347%3A1%2C0_172331%3A1%2C0_172155%3A1%2C0_172156%3A1%2C0_248627%3A1%2C0_172157%3A1%2C0_248631%3A1%2C0_172158%3A1%2C0_172357%3A1%2C0_248633%3A1%2C0_172348%3A1%2C0_172159%3A1%2C0_172160%3A1%2C0_172161%3A1%2C0_172162%3A1%2C0_172163%3A1%2C0_172164%3A1%2C0_172165%3A1%2C0_172166%3A1%2C0_172167%3A1%2C0_172168%3A1%2C0_172169%3A1%2C0_172170%3A1%2C0_172171%3A1%2C0_172172%3A1%2C0_172173%3A1%2C0_172174%3A1%2C0_172175%3A1%2C0_172176%3A1%2C0_172177%3A1%2C0_172178%3A1%2C0_172179%3A1%2C0_172181%3A1%2C0_172182%3A1%2C0_172183%3A1%2C0_172184%3A1%2C0_172185%3A1%2C0_172186%3A1%2C0_172187%3A1%2C0_172188%3A1%2C0_172189%3A1%2C0_172190%3A1%2C0_172191%3A1%2C0_172192%3A1%2C0_172193%3A1%2C0_172195%3A1%2C0_172197%3A1%2C0_172198%3A1%2C0_172199%3A1%2C0_172200%3A1%2C0_172201%3A1%2C0_172202%3A1%2C0_172203%3A1%2C0_172204%3A1%2C0_172205%3A1%2C0_172206%3A1%2C0_172207%3A1%2C0_172208%3A1%2C0_172209%3A1%2C0_172210%3A1%2C0_172211%3A1%2C0_172212%3A1%2C0_172213%3A1%2C0_172214%3A1%2C0_172215%3A1%2C0_172216%3A1%2C0_172217%3A1%2C0_172219%3A1%2C0_172220%3A1%2C0_172221%3A1%2C0_172222%3A1%2C0_172223%3A1%2C0_172330%3A1%2C0_172333%3A1%2C0_172334%3A1%2C0_172335%3A1%2C0_172336%3A1%2C0_172337%3A1%2C0_172339%3A1%2C0_172340%3A1%2C0_172341%3A1%2C0_172342%3A1%2C0_172344%3A1%2C0_248628%3A1%2C0_172345%3A1%2C0_172346%3A1%2C0_172349%3A1%2C0_172350%3A1%2C0_172352%3A1%2C0_172353%3A1%2C0_172354%3A1%2C0_172355%3A1%2C0_172356%3A1%2C0_172358%3A1%2C0_172359%3A1%2C0_172361%3A1%2C0_248629%3A1%2C0_248630%3A1%2C0_248634%3A1&AwaitingReconsent=false; _px3=e87370c9b8193ffb0a7ba21a1c67b6ed0c652fc73280074f6b4c416682bd0b26:DtgTjtAlBqWz01uiUp7FKe4l3HX6qYZ1ARwRtjBSV+TVaGWOY70jrliPiJPS2MdpgbMmaQL0Sr90DtXgV4ImLA==:1000:yc2Jrq4IbHeZuBlOL6HdR9u0phYAE3sG+V/aKgYg+w6VHsf13nTq8bRmbNGZ6KRR8i68Y1ca1yc9WviMiy/rmxPbNzQ9laH0AwL3bJVeMfxkPiBqhscnI3l5QP9IEH0+BwFshZtb5Dw5LSGnWUt1rvYbaPdjr/Lyt//mejPA5UI='
        
    })
    print(resp)
    tree = html.fromstring(html=resp.content)

    main = tree.xpath("//div[@class='AreaListingsContainer']/div/div[@class='ListingWrapper']/div/div")

    for prop in main:
        p = {
            'price': get(prop.xpath(".//div[@class='ListingCard-content-container']/div[2]/text()")),
            'size': get(prop.xpath(".//div[@class='ListingCard-content-container']/div[3]/text()")),
            'description': get(prop.xpath(".//div[@class='ListingCard-content-container']/a/h3/text()")),
            'address': get(prop.xpath(".//div[@class='ListingCard-content-container']/div[4]/text()")),
            'type': get(prop.xpath(".//div[@class='ListingCard-content-container']/div[5]/div/text()")),
        }
        extracted_data.append(p)

'''    
    next_page = tree.xpath("//a[@class='Linker PagerItem']/@href")
    if len(next_page) != 0:
        next_page_url = urljoin(base=url, url=next_page[0])
        scraper(url=next_page_url)
scraper(url='https://hotpads.com/new-york-ny/apartments-for-rent?page=')    
'''

print(len(extracted_data))
write_csv(extracted_data)
    