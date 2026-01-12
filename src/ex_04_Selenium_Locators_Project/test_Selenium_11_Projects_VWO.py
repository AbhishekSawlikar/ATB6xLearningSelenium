import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@allure.title("Negative Testcase - App.vwo.com - Wrong Email, Pass -> Error Message.")
@allure.description("Verify that if email/pass is wrong, we will get a message")
def test_verify_login_app_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")


    # Flow -> interact with the input box and enter a random username and password.
    # We need to click this submit button.
    # After waiting for some time, we need to verify the error message.

    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # vwo-html-translate-attr="placeholder"
    # vwo-html-translate-placeholder="login:enterEmailID"
    # id="login-username"
    # data-qa="hocewoqisi"
    # placeholder="Enter email ID"
    # data-gtm-form-interact-field-id="0"
    # >

    # email_web_element= driver.find_element(By.ID, "login-username")
    # email_web_element= driver.find_element(By.XPATH, "//input[@id='login-username']")
    # email_web_element= driver.find_element(By.XPATH, "//input[@name='username']")
    email_web_element= driver.find_element(By.XPATH, "//input[@data-qa='hocewoqisi']")
    email_web_element.send_keys("wrong@gmail.com")

    password_web_element = driver.find_element(By.XPATH,"//input[@name='password']")
    password_web_element.send_keys("wrong@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    # For certain time
    time.sleep(3)

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
    driver.quit()