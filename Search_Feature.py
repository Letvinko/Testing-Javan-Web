from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='Driver\chromedriver.exe')
driver.maximize_window()
driver.get("https://javan.co.id/career")
print("Page ",driver.title)

inputfield = ['Programmer Java','Programing Java Script','','/programmer-php/','00989']


def test_logic(inputfield,idx):
    time.sleep(3)
    element = driver.find_elements_by_xpath("/html/body/div[2]/section/div[2]/form/input")[0]
    element.send_keys(inputfield[idx])
    python_button = driver.find_elements_by_xpath("/html/body/div[2]/section/div[2]/form/button")[0]
    python_button.click()
    # element.clear()
    time.sleep(7)
    if idx != (len(inputfield)-1):
        python_button = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/ul/li[7]/a")[0]
        python_button.click()
    else:
        driver.quit()


for i in range(len(inputfield)):
    test_logic(inputfield,i)
