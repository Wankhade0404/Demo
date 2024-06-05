import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    global driver
    service_obj = Service(r"C:\Users\pcpoint\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

def test_Login_valid_credential(setup):
    driver.find_element(By.ID, "login2").click()
    #driver.find_element(By.XPATH, "//*[@id='sign-username']").clear()
    driver.find_element(By.ID, "loginusername").send_keys("Chhoti")
    #driver.find_element(By.XPATH, "//*[@id='sign-password']").clear()
    driver.find_element(By.ID, "loginpassword").send_keys("Chhoti@123")
    driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]").click()
    driver.switch_to.alert.accept()

def test_Login_invalid_credential(setup):
    driver.find_element(By.ID, "login2").click()
    #driver.find_element(By.XPATH, "//*[@id='sign-username']").clear()
    driver.find_element(By.ID, "loginusername").send_keys("Vaishnavi")
    #driver.find_element(By.XPATH, "//*[@id='sign-password']").clear()
    driver.find_element(By.ID, "loginpassword").send_keys("Vaishnavi@123")
    driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]").click()
    driver.switch_to.alert.accept()