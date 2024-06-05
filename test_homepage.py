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

def test_home(setup):
    driver.find_element(By.CLASS_NAME,"nav-link").click()
    driver.find_element(By.XPATH,"//*[@id='cat']").click()
    # assertion for
    message = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[2]").text
    print(message)
    assert "Phones" in message
    # click on laptops
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]").click()


