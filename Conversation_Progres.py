from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='Driver\chromedriver.exe')
driver.maximize_window()
driver.get("https://javan.co.id/contact")
print("Page ",driver.title)

inputfield = ['','007890','a0897i','@007*8','aloo']

def test_logic(inputfield,idx):
    time.sleep(3)
    python_button = driver.find_elements_by_xpath("/html/body/div[2]/section/div/div/div[1]/div/p[2]/a")[0]
    python_button.click()
    element = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/div[1]/input")[0]
    element.clear()
    element.send_keys(inputfield[idx])
    python_button = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div[2]/div/form/div[2]/button")[0]
    python_button.click()
    time.sleep(5)
    driver.back()
    if idx == (len(inputfield)-1):
        driver.quit()


for i in range(len(inputfield)):
    test_logic(inputfield,i)
