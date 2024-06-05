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

def test_addcart():
    driver.find_element(By.ID, "next2").click()
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a").click()
    driver.find_element(By.CLASS_NAME, "hrefch").click()
    driver.find_element(By.CLASS_NAME, "btn btn-success btn-lg").click()
    # driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a").click()
    driver.switch_to.alert.accept()


def test_cart():
    # checkout process
    driver.find_element(By.ID, "cartur").click()


