import requests
from bs4 import BeautifulSoup

def genuss_scraper(x):
    result = []
    url="https://genuss.ng/index.php?category_id=0&search={}&submit_search=&route=product%2Fsearch".format(x)
    http=requests.get(url)
    if http.status_code!=200:
        raise "ErrorGettingPage"
    try:
        soup=BeautifulSoup(http.text,"lxml")
        item_list = soup.find_all(class_="product-item-container")
        if (item_list!=None): 
            all_items = item_list
    except AttributeError:
        raise AttributeError
        
    def get_details():  
        lst = all_items
        for i in range(len(all_items)):
            name = lst[i].find(attrs={"class":"right-block"}).find(href=True).get_text()
            price = lst[i].find(attrs={"class":"price-new"}).find(text=True)
            link = lst[i].find(attrs={"class":"right-block"}).find(href=True).get("href")
            result.append(["Name: {}, Price: {}, Link: {}".format(name, price, link)])
    get_details()
    return result[0:3]

#print(genuss_scraper("hp laptop"))
