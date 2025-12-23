from selenium import webdriver
import allure
import pytest


@allure.title("Verify that we are able to open a page by using Selenium.")
@allure.description("We will open a page and verify that it is getting opened by using Selenium.")
def test_first_tc():
    # Selenium 3 - Not much used now
    # driver_path = '/Users/pramod/Downloads/edge/msedgedriver'
    # driver = webdriver.EdgeService(executable_path=driver_path)
    driver = webdriver.Edge()
    driver.get("https://thetestingacademy.com")
    print(driver.title)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"