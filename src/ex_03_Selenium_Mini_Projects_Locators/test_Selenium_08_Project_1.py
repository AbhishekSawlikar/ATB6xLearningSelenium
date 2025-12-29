## **Project 1 - Automating by using the Selenium Python. **
# 1. Navigate to the URL - [﻿katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
# 2. Find the **Make appointment** Button
# 3. Click on the **Make appointment **Button
# 4. Next Page will be loaded
# 5. **Find and Enter **the details **Username and Password** and **Click** on the Login Button
# 6. Verify current URL - [﻿katalon-demo-cura.herokuapp.com/#appointment](https://katalon-demo-cura.herokuapp.com/#appointment)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_project_1_katalon_positive():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # 1- Find the element the anchor tag
    # <a - open tag
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a> close tag

    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_element.click()

    # <input
    # type="text"
    # class="form-control"
    # NA- id="txt-username"
    # name="username"
    # placeholder="Username"
    # value=""
    # autocomplete="off"
    # >

    # user_name = driver.find_element(By.ID,"txt-username")
    user_name_input_box = driver.find_element(By.NAME, "username")
    user_name_input_box.send_keys("John Doe")

    # <input type="password" class="form-control" id="txt-password" name="password" placeholder="Password" value="" autocomplete="off">

    password_input_box = driver.find_element(By.NAME, "password")
    password_input_box.send_keys("ThisIsNotAPassword")

    button_signup = driver.find_element(By.ID, "btn-login")
    button_signup.click()

    time.sleep(2)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)

    driver.quit()