###############################################################################1
#IMPORT ALL NEEDED LIBRARIES AND MODULES
import nltk, re, random, sqlite3
import wikipedia as wk
from sklearn.svm import SVC
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
#from eshop_scraper import eshop_scraper
#from genuss_scraper import genuss_scraper
from jumia_scraper import jumia_scraper
#from justfone_scraper import justfone_scraper
#from kara_scraper import kara_scraper
#from pcplanet_scraper import pcplanet_scraper
#from rehmie_scraper import rehmie_scraper
#from showict_scraper import showict_scraper
#from techno_scraper import techno_scraper
#from village_scraper import village_scraper

###############################################################################2
#NLTK FOR GOOD PATTERNING
nltk.data.path.append('./nltk_data/')
stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for i in tokens:
        stemmed.append(stemmer.stem(i))
    return stemmed
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

#REMOVE STOPWORDS AND PUNCTUATIONS FROM THE USER INPUTS
stopwords_list = ["i", "my", "me", "is", "a", "an", "am", "the"]
vectorizer = TfidfVectorizer(tokenizer=tokenize, analyzer='word', lowercase=True, stop_words=stopwords_list)
def remove_punctuation(message):
    tokens = word_tokenize(message)
    #Removing Punctuations here:
    tokens_clean = [re.sub(r'[^a-zA-Z0-9{}]' ,'',each_word) for each_word in tokens] 
    tokens_final = [each_word.lower() for each_word in tokens_clean if len(each_word)]
    return tokens_final

###############################################################################3
#OPENING ALL FILES THAT ARE NEEDED
texts, labels = [],[]
with open('dataset/opening.txt', 'r', encoding='utf-8') as f:
    opening = [(i.replace('\n', ''), 'opening') for i in f.readlines()]  
    for i in opening:
        texts.append(i[0])
        labels.append(i[1])    
with open('dataset/greetings/greeting1.txt', 'r', encoding='utf-8') as f:
    greeting1 = [(i.replace('\n', ''), 'greeting1') for i in f.readlines()] 
    for i in greeting1:
        texts.append(i[0])
        labels.append(i[1])
with open('dataset/greetings/greeting2.txt', 'r', encoding='utf-8') as f:
    greeting2 = [(i.replace('\n', ''), 'greeting2') for i in f.readlines()] 
    for i in greeting2:
        texts.append(i[0])
        labels.append(i[1])
with open('dataset/greetings/greeting3.txt', 'r', encoding='utf-8') as f:
    greeting3 = [(i.replace('\n', ''), 'greeting2') for i in f.readlines()] 
    for i in greeting3:
        texts.append(i[0])
        labels.append(i[1])
with open('dataset/greetings/user_greeting1.txt', 'r', encoding='utf-8') as f:
   user_greeting1 = [(i.replace('\n', ''), 'user_greeting1') for i in f.readlines()]
   for i in user_greeting1:
       texts.append(i[0])
       labels.append(i[1]) 
with open('dataset/greetings/user_greeting2.txt', 'r', encoding='utf-8') as f:
   user_greeting2 = [(i.replace('\n', ''), 'user_greeting2') for i in f.readlines()]
   for i in user_greeting2:
       texts.append(i[0])
       labels.append(i[1]) 
with open('dataset/product_inquiry.txt', 'r', encoding='utf-8') as f:
    product_inquiry = [(i.replace('\n', ''), 'product_inquiry') for i in f.readlines()]  
    for i in product_inquiry:
        texts.append(i[0])
        labels.append(i[1])
with open('dataset/feelings/happy.txt', 'r', encoding='utf-8') as f:
    happy = [(i.replace('\n', ''), 'happy') for i in f.readlines()]
    for i in happy:
        texts.append(i[0])
        labels.append(i[1])
with open('dataset/feelings/sad.txt', 'r', encoding='utf-8') as f:
    sad = [(i.replace('\n', ''), 'sad') for i in f.readlines()]  
    for i in sad:
        texts.append(i[0])
        labels.append(i[1])  
with open('dataset/faq.txt', 'r', encoding='utf-8') as f:
    faq = [(i.replace('\n', ''), 'faq') for i in f.readlines()]
    for i in faq:
        texts.append(i[0])
        labels.append(i[1])
with open('dataset/user_input.txt', 'r', encoding='utf-8') as f:
    user_input = [(i.replace('\n', ''), 'user_input') for i in f.readlines()]  
    for i in user_input:
        texts.append(i[0])
        labels.append(i[1]) 
with open('dataset/end.txt', 'r', encoding='utf-8') as f:
    end = [(i.replace('\n', ''), 'end') for i in f.readlines()]  
    for i in end:
        texts.append(i[0])
        labels.append(i[1])
    
###############################################################################5
#CLASSIFICATION OF THE FILES AND USER INPUTS
X_vector = vectorizer.fit_transform(texts)
clf = SVC(kernel='linear',probability=True)
clf.fit(X_vector,labels)
def classifier(message):
    out_put = []
    message_tokens = remove_punctuation(message)
    message_string = (' '.join(message_tokens))
    out_put.append(message_string)
    out_put_vector = vectorizer.transform(out_put)
    #print(clf.predict_proba(out_put_vector))
    out_put_class = clf.predict(out_put_vector)
    return out_put_class[0]

###############################################################################6
#PRODUCT INQUIRY
available_products = ["laptops"]
alt_spellings = ["laptop"]
spellings_dict = {"laptop":available_products[0]}
brand = ["apple", "hp", "acer", "asus", "lenovo", "microsoft", "dell", "toshiba","fujitsu", "huawei"]

def jumia_laptop(a):
    if a in brand:
        x="laptops/{0}".format(a)
        lst=jumia_scraper(x)
        if len(lst) != 0:
            for i in lst:
                return i
        else:
            return "Wasn't able to get that at the moment...\nMaybe not currently available." 
    else:
        return "Sorry, We don't have such laptop in our database\nPlease check your spelling"


#SPECIFY TYPE OF LAPTOP
def available():
    text="The Laptop Brands available for now are\nHP\nApple\nDell\nAcer\nAsus\nLenovo\nMicrosoft\nToshiba\nfujitsu"
    return text
def specify():
    details=["You have to specify","Brand: ","Type: ","Price range(Optional): "]
    print(details[0])
    print(available())
    laptop_brand=input(details[1])
    if (laptop_brand.lower() not in brand):
        print('Sorry, {} laptop is not available'.format(laptop_brand))
        laptop_brand=input(details[1])
    laptop_type=input(details[2])
    laptop_price=input(details[3])
    
    #Connect User Input to database
    con = sqlite3.connect('laptop.db')
    co = con.cursor()
    def create_table():
        co.execute('CREATE TABLE IF NOT EXISTS '+username+'(brand TEXT, type TEXT, price TEXT)')
    def data_entry(a,b,c):
        co.execute("INSERT INTO "+username+" VALUES (?,?,?)",(a,b,c))
        con.commit()
        co.close()
        con.close()
    create_table()
    data_entry(laptop_brand,laptop_type,laptop_price)
    print("Okay... Request loading...")
    print("Checking Jumia")
   
    j_laptop=jumia_scraper(laptop_brand+"/"+laptop_type)
    print(j_laptop)
    
###############################################################################7
#OPENING TAG
display=""
speaker = ["Chappy:", "User: "]
welcome=["Hello, Start Conversation","Hi my name is Chappy. What's your name? "]
print(speaker[0],welcome[0])
first_input=input(speaker[1])
print('\n'+speaker[0],welcome[1])
username=input(speaker[1])
new_user=username.lower()
if "i\'m " in new_user:
    username=new_user[4:]
elif "my name is " in new_user:
    username=new_user[11:]
elif "i am " in new_user:
    username=new_user[5:]
    
def opening_tag():    
    i=random.choice(opening)  
    display=i[0] + username.capitalize()
    print('\n'+speaker[0],display) 
    j=random.choice(greeting1)
    display2=username.capitalize()+ ", " +j[0]
    print('\n'+speaker[0],display2)
    input(speaker[1])
    k=random.choice(greeting3)  
    display3=username.capitalize()+ ", " + k[0]
    print('\n'+speaker[0],display3)
opening_tag()
    
###############################################################################8
##CHATBOT FLOW
def response(message):
    if message=="faq":
        return "Thinking..."
    elif message == "greeting1": 
        i=random.choice(greeting2)  
        return i[0]
    elif message == "user_greeting1":
        i=random.choice(user_greeting2)
        return i[0]
    elif message == "product_inquiry":
       return specify()  
    elif message == "happy":
        return "Good to know"
    elif message == "sad":
        return "I'm sorry. I will ask my programmer to improve on me"
    elif message == "end":
        return "Cool... Thanks. Have a nice day"
    elif message == "user_input":
        return "Do not know what that mean. I am checking Wikipedia.."
    
def questions(message):
    with open('dataset/faq.txt', 'r', encoding='utf-8') as f:
        for i in f:
            reply = f.readline()
            if reply.startswith(message) != -1: 
                real=reply.split("-")
                #print(reply)
                return real[1]

def wiki(message):
   try:
       wiki = wk.summary(message, sentences = 2)
       return wiki
   except:
       return "No content has been found"

        
###############################################################################10
#LOOP THE CHATBOT
flag=True
while flag:
    sentence=input(speaker[1])
    result = classifier(sentence)
    resp=response(result)
    print(speaker[0], resp)
    if resp=="Thinking...":
        print(speaker[0], questions(sentence))
    elif resp=="Do not know what that mean. I am checking Wikipedia..":
        print(speaker[0], wiki(sentence))
    elif resp=="Cool... Thanks. Have a nice day":
        flag=False

###############################################################################11