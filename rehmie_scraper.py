import requests
from bs4 import BeautifulSoup

def rehmie_scraper(x):
    result = []
    url="https://rehmie.com/search?q={}".format(x)
    http=requests.get(url)
    if http.status_code!=200:
        raise "ErrorGettingPage"
    try:
        soup=BeautifulSoup(http.text,"lxml")
        item_list = soup.find_all(class_="col-xl-3 col-sm-4 col-6 product text-center")
        if (item_list!=None): 
            all_items = item_list
    except AttributeError:
        raise AttributeError
     
    def get_details():  
        lst = all_items
        for i in range(len(all_items)):
            name = lst[i].find(attrs={"class":"productContent pt-3"}).find(href=True).get_text()
            price = lst[i].find(attrs={"class":"d-inline-block mrp"}).get_text()
            link = "https://rehmie.com" + lst[i].find(attrs={"class":"productContent pt-3"}).find(href=True).get("href")
            result.append(["Name: {}, Price: {}, Link: {}".format(name, price, link)])
    get_details()
    return result[0:3]

#print(rehmie_scraper("hp laptop"))
