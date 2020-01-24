import requests
from bs4 import BeautifulSoup

def village_scraper(x):
    result = []
    url="https://computervillage.ng/catalogsearch/result/?q={}".format(x)
    http=requests.get(url)
    if http.status_code!=200:
         raise "ErrorGettingPage"
    try: 
        soup=BeautifulSoup(http.text,"lxml")
        item_list = soup.find_all(class_="product-item-info type1")
        if (item_list!=None): 
            all_items = item_list
    except AttributeError:
        raise AttributeError
     
    def get_details():  
        lst = all_items
        for i in range(len(all_items)):
            name = lst[i].find(attrs={"class":"product-item-link"}).find(text=True).strip()
            price = lst[i].find(attrs={"class":"price"}).get_text()
            link = lst[i].find(attrs={"class":"product-item-link"})['href']
            result.append(["Name: {}, Price: {}, Link: {}".format(name, price, link)])
    get_details()
    return result[0:2]

#print(village_scraper("dell laptop"))
