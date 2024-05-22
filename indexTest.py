# imports
# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# set driver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

# functions

# test1: dupla kattintás után szerepel-e az "animation" class
def test1 ():
    elementOne = driver.find_element(By.ID, value="element-one")
    ActionChains(driver).double_click(elementOne).click().perform()
    ActionChains(driver).move_to_element(elementOne).perform()
    

test1()
driver.save_screenshot('test1.png')

time.sleep(1)

# ha rámegy az egér, utána létezik-e box-shadow
# test3()
def test2():
    elementTwo = driver.find_element(By.ID, value="element-two")
    ActionChains(driver).move_to_element(elementTwo).perform()
test2()
    
    
driver.save_screenshot('test2.png')
time.sleep(1)
# kattintás után eltűnik-e
def test3 ():
    elementThree = driver.find_element(By.ID, value="element-three")
    ActionChains(driver).click(elementThree).perform()
test3()
driver.save_screenshot('test3.png')

time.sleep(1)
# kattintás után a háttere zöld lesz-e
def test4 ():
    elementFour = driver.find_element(By.ID, value="element-four")
    ActionChains(driver).click(elementFour).perform()
    
test4()
driver.save_screenshot('test4.png')

time.sleep(1)
# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
def test5 ():
    elementFour = driver.find_element(By.ID, value="element-four")
    ActionChains(driver).move_to_element(elementFour).perform()
test5()
driver.save_screenshot('test5.png')
