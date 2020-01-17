import requests
from bs4 import BeautifulSoup

def techno_scraper(x):
    result = []
    url = "https://www.technocratng.com/?s={}&post_type=product".format(x)
    http=requests.get(url)
    if http.status_code!=200:
        raise "ErrorGettingPage"
    try:
        soup=BeautifulSoup(http.text,"lxml")
        item_list = soup.find_all(class_="product-wrapper")
        if (item_list!=None): 
            all_items = item_list       
    except AttributeError:
        raise AttributeError
        
    def get_details():  
        lst = all_items
        for i in range(len(all_items)):
            name = lst[i].find(attrs={"class":"heading-title product-name"}).find(text=True).strip()
            price = (lst[i].find(attrs={"class":"price"}).get_text()).split(" ")[1]
            link = lst[i].find(attrs={"class":"heading-title product-name"}).find(href=True).get("href")
            result.append(["Name: {}, Price: {}, Link: {}".format(name, price, link)])
    get_details()
    return result[0:3]

#print(techno_scraper("asus laptop"))
