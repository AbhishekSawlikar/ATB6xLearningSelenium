from selenium import webdriver
import allure
import pytest


@allure.title("Print the Page Source of the page.")
def test_selenium():
    # Selenium 4
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/") # Navigate to URL
    page_source_as_html = driver.page_source
    print(driver.title)
    print(driver.current_url)
    assert "CURA Healthcare Service" in page_source_as_html


    # I will explin, but it means close all the browser windows.
    driver.quit()