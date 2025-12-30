from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run_login_test(username, password, expected_text, screenshot_name):
    driver = webdriver.Chrome()  # Or webdriver.Firefox() if preferred
    driver.get("http://your-login-page-url.com/login")  # TODO: Update to your login page URL

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(2)  # Wait for page to load

    driver.save_screenshot(screenshot_name)
    page_source = driver.page_source
    driver.quit()
    return expected_text in page_source

if __name__ == "__main__":
    # Valid credentials test
    success = run_login_test("validUser", "validPass", "Welcome", "valid_login.png")
    print("Valid login test passed:", success)

    # Invalid credentials test
    failure = run_login_test("invalidUser", "wrongPass", "Invalid credentials", "invalid_login.png")
    print("Invalid login test passed:", failure)
