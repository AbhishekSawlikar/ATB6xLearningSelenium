import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    # Wait for map to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "svg"))
    )
    yield driver
    driver.quit()


def test_non_existent_state(setup):
    driver = setup
    non_existent_state = "Atlantis"  # Or "ABCState" - triggers NoSuchElementException

    element_found = False
    try:
        # This will raise NoSuchElementException
        state_element = driver.find_element(By.CSS_SELECTOR, f"path[title='{non_existent_state}']")
        element_found = True
    except NoSuchElementException:
        logging.info(f"Expected NoSuchElementException for '{non_existent_state}' - handled successfully")
        element_found = False

    assert not element_found, f"Unexpected: Element for '{non_existent_state}' was found!"

    # Alternative: Verify using find_elements (returns empty list)
    states = driver.find_elements(By.CSS_SELECTOR, f"path[title='{non_existent_state}']")
    assert len(states) == 0, "Non-existent state elements found!"
