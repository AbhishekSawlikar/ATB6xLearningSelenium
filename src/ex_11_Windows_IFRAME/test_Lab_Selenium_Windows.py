import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_windows():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle
    print(parent_window)
    # 2289D93D36A9FAC1BD7F1D576190BE06

    link = driver.find_element(By.XPATH, "//a[contains(text(),'Click Here')]")
    link.click()
    #  link = driver.find_element(By.LINK_TEXT, "Click Here")

    window_handles = driver.window_handles
    # ['ACFDB277EB0B25676AD5F907ED2D25E0', 'F3CE099FAAAE1D4D6C9BB420334F9EC0']

    print(window_handles)

    for handle in window_handles:
        if handle != parent_window:
            driver.switch_to.window(handle)
            if "New Window" in driver.page_source:
                print("Test Passed!")
                break

    # driver.switch_to.window(window_handles[1])