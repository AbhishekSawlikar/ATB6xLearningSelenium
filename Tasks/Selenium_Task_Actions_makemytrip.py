import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



@allure.title("Make My Trip website - elements interactions")
@allure.description("To verify that the script can interact with webelements of makemytrip website")

def test_makemytrip():

    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    # //span[@data-cy="closeModal"] wait -> click
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
    )
    driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()

    time.sleep(2)

    # To bypass the element shown near from city
    background_element = driver.find_element(By.TAG_NAME, "body")
    background_element.click()

    # Enter into From City
    # Move mouse cursor to fromCity -> Click on it -> Input text - 'del'

    fromCity = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    (actions.move_to_element(fromCity)
     .click()
     .send_keys_to_element(fromCity, "DEL")
     .perform())

    time.sleep(2)

    # Press Down Arrow to select "New Delhi" -> Press key Enter
    (actions.move_to_element(fromCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform())

    time.sleep(2)

    # Enter into To City
    # Move mouse cursor to toCity -> Click on it -> Input text - 'del'

    toCity = driver.find_element(By.ID, "toCity")
    actions = ActionChains(driver)
    (actions.move_to_element(toCity)
     .click()
     .send_keys_to_element(toCity, "IXC")
     .perform())

    time.sleep(2)

    # Press Down Arrow to select "Chandigarh" -> Press key Enter
    (actions.move_to_element(toCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform())

    time.sleep(5)

    driver.quit()