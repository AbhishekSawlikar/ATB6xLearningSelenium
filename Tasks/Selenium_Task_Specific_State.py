import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    yield driver
    driver.quit()

def test_click_maharashtra(setup):
    driver = setup
    max_retries = 3
    logging.basicConfig(level=logging.INFO)

    for attempt in range(max_retries):
        try:
            # Scroll into view and wait for clickable state (better than presence)
            maharashtra = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "path[aria-label='Maharashtra']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", maharashtra)
            maharashtra.click()

            # Validate tooltip with text presence
            tooltip = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "path[aria-label='Maharashtra']"))
            )
            assert "Maharashtra" in tooltip.text
            logging.info("Test passed on attempt %d", attempt + 1)
            return  # Success, exit retry loop

        except TimeoutException as e:
            logging.warning("Timeout on attempt %d: %s", attempt + 1, str(e))
            if attempt == max_retries - 1:
                pytest.fail(f"Failed after {max_retries} retries: Could not locate or interact with Maharashtra/tooltip")
            # Optional: Add short sleep or page refresh for flakiness
            driver.refresh()
