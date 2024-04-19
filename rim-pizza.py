import requests
from bs4 import BeautifulSoup
base_url = 'https://dominopizza.ru/'
response = requests.get(url=base_url,verify=False)
soup = BeautifulSoup(response.test,'html.parser')
div_rim = soup.find('div', {'id': 'rimskaya'})
div_cls_cols = div_rim.find_all('div',{'class':'col'})
pizza_list = []

for div_cls_col in div_cls_cols:
    pizza_detail = div_cls_col.a.div.find(
        'div',{'class': 'product-card-content'}
        )
    pizza_name = pizza_detail.find(
        'div', {'class':'product-name'}
        ).get_text()
    pizza_describtion = pizza_detail.find(
        'p': {'class': 'product-describtion'}
        )   
    pizza_price = pizza_detail.find(
        'div', {'class':'price'}
    )
    print(pizza_name)
    print(pizza_describtion)
    print(pizza_price)
    print('----------------------')