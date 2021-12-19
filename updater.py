import time, os, sys, platform
try:
    import requests, wget
except: print('do "pip install -r requirements.txt" in console'); time.sleep(2); sys.exit() 
link = "https://website.com/updater.exe"; logo = "Updater"
def title(message=None):
    if message is None: message = 'Updater Title'
    if platform.platform().startswith('Windows'): os.system('title {}'.format(str(message)))
def clear():
    if platform.platform().startswith('Windows'): os.system('cls')
    else: os.system('clear')
try:
    title();clear();print(logo);print('\n Updater\n\n Please eneter your sellix id.')
    try: order_id = input(' > ')
    except: print(' You cannot bypass that :D'); time.sleep(2); sys.exit()
    try:
        url = "https://dev.sellix.io/orders/{}".format(str(order_id))
        headers = {"Authorization": "Bearer testingjHdAZK6jG2pN6cabSQdZhlS2XqE8UvOSdqSDtlZAeOuF2jfr3a87KKs3Z"}
        r = requests.get(url, headers=headers)
        if "uniqid" in r.text:
            print(' Installing files.')
            if platform.platform().startswith('Windows'): wget.download(link)
            else: print(' Other platforms are not ready yet.'); time.sleep(2); sys.exit()
        elif "Not Found" in r.text: print(' Please specify a real order.'); time.sleep(2); sys.exit()
        else: print(' Cannot get the output. Try again later.'); time.sleep(2); sys.exit()
    except: print(' Sellix might be down, please try again later.'); time.sleep(2); sys.exit()
except requests.ConnectionError: print(' Our panels are down, please try again later.'); time.sleep(2); sys.exit()
except: print(' Please try again later!'); time.sleep(2); sys.exit()
