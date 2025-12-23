from selenium import webdriver
import allure
import pytest


@allure.title("Verify that we are able to open a page by using Selenium.")
@allure.description("We will open a page and verify that it is getting opened by using Selenium.")
def test_first_tc():
    # Selenium 4
    driver = webdriver.Firefox()
    driver.get("https://thetestingacademy.com")
    print(driver.title)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"