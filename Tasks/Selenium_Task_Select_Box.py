import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.fixture
def setup():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    yield driver
    driver.quit()


def test_select_box_interaction(setup):
    driver = setup
    dropdown = driver.find_element(By.ID, "continents")
    select = Select(dropdown)

    # Select by visible text
    select.select_by_visible_text("Europe")
    assert select.first_selected_option.text == "Europe"

    # Select by index (adjust index based on actual order)
    select.select_by_index(3)
    assert select.first_selected_option.text == "Australia"

    # Select by visible text instead of value
    select.select_by_visible_text("Africa")
    assert select.first_selected_option.text == "Africa"
