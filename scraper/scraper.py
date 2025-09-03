# import requests
# from bs4 import BeautifulSoup
# import json

# # url1='https://books.toscrape.com'
# url1='https://books.toscrape.com/catalogue/page-{}.html'
# response=requests.get(url=url1)
# html_response =response.text

# soup=BeautifulSoup(html_response, 'html.parser')
# # print(html_response)
# products=[]

# product_elements =soup.select('article.product_pod')

# for product_element in product_elements:
#     product_name=product_element.select_one('h3 a')['title']
#     # print("producgt name:", product_name)
#     product_price=product_element.select_one('.price_color').text.strip().replace('Â', '')


#     products.append({
#         'name':product_name,
#         'price': product_price
#     })
# json_output = json.dumps(products, indent=4) # indent for pretty printing
# print(json_output)


#improved code base:
import requests
from bs4 import BeautifulSoup
import json 

baseurl="https://books.toscrape.com/catalogue/page-{}.html"
# baseurl="https://www.amazon.in/s?k=mobile+phones&i=electronics&page=&xpid=HAAGefPz49AHT&crid=3JEV7SWO421EY&qid=1756698774&sprefix=mobile+phone%2Celectronics%2C356&ref=sr_pg_2"

products=[]

for page in range(1,51):
    url=baseurl.format(page)
    response=requests.get(url=url)

    if response.status_code!=200: # error
        break
    response=response.text
    soup=BeautifulSoup(response, 'html.parser')
    product_elements=soup.select('article.product_pod')

    for product in product_elements:
        name=product.select_one("h3 a")["title"]
        price=product.select_one(".price_color").text.strip().replace("Â", "")
        products.append({"name":name,"price":price})
    
# print(products)
with open("data/books.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)