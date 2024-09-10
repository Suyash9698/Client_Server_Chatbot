import time
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyttsx3
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
html_file = os.getcwd() + "//" + "main.html"
print(html_file)
options.add_argument("--app="+html_file)
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service,options=options)

driver.get("file:///" +html_file)

s=driver.find_element(By.ID,'textInput')
k=driver.find_element(By.ID,'khushi')
container = driver.find_element(By.ID,"skl")
khushi=driver.find_element(By.ID,'love')
khushi2=driver.find_element(By.ID,'love2')

speaker1=driver.find_element(By.ID,'ok')
speaker2=driver.find_element(By.ID,'ok2')
#sk=driver.find_element_by_id('pop')
#temp="ko"
#driver.execute_script("document.getElementById('none').innerHTML='"+temp+"'")
#para=driver.find_element_by_id('we')

subprocess.call(["say", "-v", "Samantha","Please wait while we are connecting with you"])
df=k.get_attribute('value')
import socket
def server_program():
    # get the hostname
    host='192.168.33.59'
    #s=socket.gethostbyname(socket.gethostname())
    port = 2303  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together


    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            driver.execute_script("arguments[0].style.display = 'none';", container)
            s.send_keys("Thankyou"+"\U0001F60A"+". This conversation was closed.")
            k.click()
            khushi.click()
            driver.execute_script("arguments[0].style.display = 'none';", s)
            driver.execute_script("arguments[0].style.display = 'none';", k)
            driver.execute_script("arguments[0].style.display = 'none';", khushi)
            driver.execute_script("arguments[0].style.display = 'none';", khushi2)
            driver.execute_script("arguments[0].style.display = 'none';", speaker1)
            driver.execute_script("arguments[0].style.display = 'none';", speaker2)
            subprocess.call(["say", "-v", "Samantha","Thankyou. This conversation was closed."])
            break
        driver.execute_script("arguments[0].style.display = 'none';", container)
        print("from connected user: " + str(data))
        s.send_keys(str(data))
        k.click()
        khushi.click()
        k.click()
        subprocess.call(["say", "-v", data])

        
        lol = k.get_attribute('value')
        sf = lol
        while lol == sf:
            sf = k.get_attribute('value')
            #print(sf +"ab gaya")
        s.send_keys(sf)
        k.click()
        khushi2.click()
        lol = sf
        data =k.get_attribute('value')
        print(data)
        if data.lower().strip()=='bye':
            data="Thankyou" + "\U0001F60A" + ". This conversation was closed."
            conn.send(data.encode())
            driver.execute_script("arguments[0].style.display = 'none';", s)
            driver.execute_script("arguments[0].style.display = 'none';", k)
            driver.execute_script("arguments[0].style.display = 'none';", khushi)
            driver.execute_script("arguments[0].style.display = 'none';", khushi2)
            driver.execute_script("arguments[0].style.display = 'none';", speaker1)
            driver.execute_script("arguments[0].style.display = 'none';", speaker2)
            subprocess.call(["say", "-v", "Samantha","Thankyou. This conversation was closed."])
            break
        conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection

server_program()