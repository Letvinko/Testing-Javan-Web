from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='Driver\chromedriver.exe')
driver.maximize_window()
driver.get("https://javan.co.id/career")
print("Page ",driver.title)

trackID = ['','2cb7cc42-9e5a-11eb-8a50-d60b1cd6c962','','2cb7cc42-9e5a-11eb-8a50-d60b1cd6c962','124871-12843ad-daskljd-23ad-adks;k9']
email = ['','','adityamaulana964@gmail.com','aaaa','adityamaulana964@gmail.com']

def test_logic(inputfield,idx):
    time.sleep(3)
    python_button = driver.find_elements_by_xpath("/html/body/div[2]/section/div[2]/button")[0]
    python_button.click()
    elementTrackID = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/form/div[1]/input")[0]
    elementTrackID.send_keys(trackID[idx])
    elementEmail = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/form/div[2]/input")[0]
    elementEmail.send_keys(email[idx])
    python_button = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/form/div[3]/button")[0]
    python_button.click()
    time.sleep(5)
    driver.back()
    if idx == (len(trackID)-1):
        driver.quit()


for i in range(len(trackID)):
    test_logic(trackID,i)
