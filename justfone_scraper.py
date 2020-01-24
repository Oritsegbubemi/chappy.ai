import requests
from bs4 import BeautifulSoup

def justfone_scraper(x):
    result = []
    url="https://justfones.ng/catalogsearch/result/?cat=&q={}".format(x)
    http=requests.get(url)
    if http.status_code!=200:
        raise "ErrorGettingPage"
    try:
        soup=BeautifulSoup(http.text,"lxml")
        item_list = soup.find_all(class_="item last")
        if (item_list!=None): 
            all_items = item_list
    except AttributeError:
        raise AttributeError
        
    def get_details():  
        lst = all_items
        for i in range(len(all_items)):
            name = lst[i].find(class_="product-name").find(text=True)
            price = lst[i].find(class_="price").getText()
            link = lst[i].find(attrs={"class":"product-name"}).find(href=True).get("href")
            result.append(["Name: {}, Price: {}, Link: {}".format(name, price, link)])
    get_details()
    return result[0:3]

#print(justfone_scraper("hp laptop"))
