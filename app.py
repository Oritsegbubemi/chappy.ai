#Trying to get the last message

import requests
import time
from chappy_telegram import classifier, response, user_type, search_product, wiki
last_saved_message = ''

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        
    def get_updates(self, offset=None, timeout=20):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        method = 'sendMessage'
        params = {'chat_id': chat_id, 'text': text}
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
             last_update = get_result[len(get_result)]
        return last_update
    """
    def get_new_message(self):
        global last_saved_message
        current_last_message = self.get_last_update()['update_id']['message']['text']

        # Check for new message
        if current_last_message == last_saved_message:
            time.sleep(10)  # no new message wait for new message
            self.get_new_message()
        else:
            last_saved_message = current_last_message
            return current_last_message
"""

token = '943273135:AAHXI6GPMSKatsSJz3e3xOpEcqHmlnFVBns'
chappy_ai = BotHandler(token)

available_products = ["laptops"]
alt_spellings = ["laptop"]
spellings_dict = {"laptop":available_products[0]}
laptop_brand = ["apple", "hp", "acer", "asus", "lenovo", "microsoft", "dell", "toshiba","fujitsu", "huawei"]
enter_brand = ""
enter_type = ""

def main():
    print("Start")
    new_offset = None
    while True:
        chappy_ai.get_updates(new_offset)
        try:
            last_update = chappy_ai.get_last_update()
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']
            lower_case_text = last_chat_text.lower()
            
            #Begining of conversation with bot
            if lower_case_text == "/start":
                #print(lower_case_text)
                bot_msg = "Hello {}, i am Chappy and i help you get best prices for products you desire".format(last_chat_name)
                chappy_ai.send_message(last_chat_id, bot_msg)
                
            #Main conversation with bot
            else:
                result = classifier(lower_case_text)
                
                if result == "product_inquiry": #Only repsonds to product inquiry
                    bot_msg = user_type() #Call the user_specify function
                    chappy_ai.send_message(last_chat_id, bot_msg)
                    #lower_case_text = chappy_ai.get_new_message()
                    print(lower_case_text)
                    bot_msg = search_product(lower_case_text) #Call search_product function
                    chappy_ai.send_message(last_chat_id, bot_msg)
                    
                    
                elif result == "user_input":
                    bot_msg = 'Do not know what that mean. I am checking Wikipedia..'
                    chappy_ai.send_message(last_chat_id, bot_msg)
                    bot_msg = wiki(lower_case_text)
                    chappy_ai.send_message(last_chat_id, bot_msg)
                
                else:
                    bot_msg = response(result)
                    #print(lower_case_text)
                    chappy_ai.send_message(last_chat_id, bot_msg)
                        
            new_offset = last_update_id + 1
            
        except Exception:
            pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

"""        
url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
# reply with a photo to the name the user sent,
# note that you can send photos by url and telegram will fetch it for you
bot.sendChatAction(chat_id=chat_id, action="upload_photo")
sleep(2)
bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
"""