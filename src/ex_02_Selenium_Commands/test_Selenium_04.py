from selenium import webdriver
import allure
import pytest


@allure.title("Print the Page Source of the page.")
def test_selenium():
    # Selenium 4
    driver = webdriver.Edge()
    driver.get("https://thetestingacademy.com")
    print(driver.page_source)