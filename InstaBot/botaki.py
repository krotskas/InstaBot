import os
os.system('pip install selenium')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



class InstaBot:
    def __init__(self, username, password):
        self.username=username
        self.password=password
        path_driver=os.path.abspath(('chromedriver.exe'))
        self.driver = webdriver.Chrome(path_driver)

    def login(self):
        driver=self.driver
        driver.get('https://www.instagram.com/')
        sleep(2)
        username_button=driver.find_element_by_xpath("//input[@name=\"username\"]")
        username_button.send_keys(self.username)
        password_button=driver.find_element_by_xpath("//input[@name=\"password\"]")
        password_button.send_keys(self.password)
        password_button.send_keys(Keys.RETURN)
        sleep(3)


    def page(self,link):
        self.driver.get(link)
        sleep(3)

    
    def comment(self,url,comment):
        self.page(url)
        sleep(2)
        commentArea = self.driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        sleep(2)
        commentArea = self.driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        commentArea.clear()
        commentArea.send_keys(comment)
        sub=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[@type='submit']")
        sub.click()


    def like(self,url):
        self.page(url)
        sleep(2)
        likeArea = self.driver.find_element_by_class_name('_8-yf5 ')
        likeArea.click()


username=input('Dwse to username sou: ')
password=input('Dwse to password sou: ')

link=input('Dwse to link pou thleis: ')
num=int(input('posa sxolia theleis na kanei epanalhpsh: '))
sxolia=[]
for i in range(num):
    comment=input('dwse sxolio: ')
    sxolia.append(comment)

time=int(input('dwse ta defterolpeta pou theleis na perimenei h efarmogh mexri to epomeno sxolio: '))

user=InstaBot(username , password)
user.login()
while True:
    for i in range(num):
        user.comment(link,sxolia[i])  
        sleep(time)

