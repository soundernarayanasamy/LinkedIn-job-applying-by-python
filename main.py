import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

MAIL = ENTER_YOUR_MAIL
PASSWORD = ENTER_YOUR_PASSWORD
PHONE = ENTER_YOUR_NUMBER

def close_application():
    # Click Close Button
    close = driver.find_element(by=By.CLASS_NAME, value="artdeco-button__icon")
    close.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-button__text")[1]
    discard_button.click()

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3731047869&geoId=102713980&keywords=assistante&location=India&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")
time.sleep(2)

# Directly goes to LinkedIn signin page
sign_in = driver.find_element(By.LINK_TEXT, value='Sign in')
sign_in.click()

# Enters the E-mail and Password
email = driver.find_element(By.ID, value="username")
email.clear()
email.send_keys(MAIL)

password = driver.find_element(By.ID, value="password")
password.clear()
password.send_keys(PASSWORD)

sign_inn = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]')
sign_inn.click()

input("Press Enter when you have solved the Captcha")

time.sleep(5)
job_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".jobs-search-results-list")

# Apply for Jobs
for listing in job_listings:
    listing.click()
    time.sleep(3)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button--top-card")
        apply_button.click()

        # Insert Phone Number
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
             phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        close_application()
        print("No application button, skipped.")
        continue

driver.quit()
