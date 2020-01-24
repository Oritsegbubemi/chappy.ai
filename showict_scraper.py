import requests
from bs4 import BeautifulSoup

def showict_scraper(x):
    result = []
    url="https://showict.com.ng/?s={}&post_type=product".format(x)
    http=requests.get(url)
    if http.status_code!=200:
        raise "ErrorGettingPage"
    try:
        soup=BeautifulSoup(http.text,"lxml")
        item_list = soup.find_all(class_="mf-product-details")
        if (item_list!=None): 
            all_items = item_list
    except AttributeError:
        raise AttributeError
        
    def get_details():  
        lst = all_items
        for i in range(len(all_items)):
            name = lst[i].find(attrs={"class":"mf-product-details-hover"}).find(text=True)
            price = lst[i].find(attrs={"class":"price"}).getText()
            link = lst[i].find(attrs={"class":"mf-product-content"}).find(href=True).get("href")
            result.append(["Name: {}, Price: {}, Link: {}".format(name, price, link)])
    get_details()
    return result[0:2]

#print(showict_scraper("hp laptop"))
