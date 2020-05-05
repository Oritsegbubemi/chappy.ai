import requests
from bs4 import BeautifulSoup

def jumia_scraper(x):
    result = []
    url = "https://www.jumia.com.ng//catalog/?q={}".format(x)
    http = requests.get(url)
    if http.status_code!=200:
        raise "ErrorGettingPage"
    try:
        soup = BeautifulSoup(http.text,"lxml")
        item_list1 = soup.find_all(class_="sku -gallery")
        item_list2 = soup.find_all(class_="mabaya sku -gallery")
        item_list3 = soup.find_all(class_="sku -gallery -has-offers")
        if (item_list1!=None and item_list2!=None and item_list3!=None): 
            all_items = item_list1 + item_list2 + item_list3
    except AttributeError:
        raise AttributeError
        
    def get_details():  
        lst = all_items
        for i in range(len(all_items)):
            brand = lst[i].find(attrs={"class":"brand"}).find(text=True).strip()
            name = lst[i].find(attrs={"class":"name"}).find(text=True).strip()
            price = lst[i].find(attrs={"class":"price"}).find(attrs={"dir":"ltr"}).find(text=True)
            link = lst[i].find(attrs={"class":"link"})["href"].strip()
            result.append(["Name: {} {}, Price: {}, Link: {}".format(brand, name, price, link)])
    get_details()
    return result[0:3]

print(jumia_scraper("dell laptop corei3"))
