import time
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import subprocess

PATH="/Users/suyash9698/Downloads/chromedriver-mac-arm64/chromedriver"
options = webdriver.ChromeOptions()
#options.add_experimental_option("useAutomationExtension", False)
#options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument('--disable-gpu')
options.add_argument('--window-position=955,127')

#options.add_argument('--disable-infobars')
options.add_argument('--window-size=580,700')
options.add_argument("--no-sandbox")
html_file = os.getcwd() + "//" + "mainForServer.html"
print(html_file)
options.add_argument("--app="+html_file)
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service,options=options)

driver.get("file:///" +html_file)

s=driver.find_element(By.ID,'textInput')
k=driver.find_element(By.ID,'khushi')  # this is a send button
container = driver.find_element(By.ID,"skl") # ye hai left me aayega message to change kro to right
khushi=driver.find_element(By.ID,'love') # append message to left
khushi2=driver.find_element(By.ID,'love2') # to right

speaker1=driver.find_element(By.ID,'ok') #button hai speaker ka related
speaker2=driver.find_element(By.ID,'ok2')#speaker
#sk=driver.find_element_by_id('pop')
#temp="ko"
#driver.execute_script("document.getElementById('none').innerHTML='"+temp+"'")
#para=driver.find_element_by_id('we')

subprocess.call(["say", "-v", "Samantha","Please wait while we are connecting with you"])
df=k.get_attribute('value')
import socket
def actual_server_program():
    host ='192.168.33.59'  # as both code is running on same pc
    port = 2303  # socket server port number

    client_socket = socket.socket()  # instantiate
    while True:
        try:
            print("Trying to Find Client...")
            client_socket.connect((host, port))  # connect to the server
            break  # exit the loop if connection is successful
        except socket.error as e:
            print(f"Connection failed: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)  # wait for 5 seconds before retrying

    #data = input(" -> ")  # take input
    data = k.get_attribute('value')

    print(data)

    lol = data

    while lol == data:
        data = k.get_attribute('value')

    while data.lower().strip() != 'bye' :
        s.send_keys(str(data))
        k.click()
        khushi.click()
        k.click()
        subprocess.call(["say", "-v", data])
        client_socket.send(data.encode())  # send message
        
        

        data = client_socket.recv(1024).decode()  # receive response

        print("from connected user: " + str(data))
        s.send_keys(str(data))
        k.click()
        khushi2.click()
        k.click()
        subprocess.call(["say", "-v", data])

        print('Received from server: ' + data)  # show in terminal

       

        #data = input(" -> ")  # again take inpu
        
        data = k.get_attribute('value')
       
        sf = data
        while data == sf:
            data = k.get_attribute('value')

    client_socket.close()  # close the connection

    
   
actual_server_program()