from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


email_addr = EMAIL_ADDR
password = PASS


driver = webdriver.Chrome(executable_path="/Users/theo/Downloads/chromedriver")

job = "software developer"

driver.get("https://www.linkedin.com/jobs/search?keywords=software%20developer&location=London%2C%20England%2C%20United%20Kingdom&geoId=102257491&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
driver.set_window_size(width=1500, height=1000)

sign_in_button = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_in_button.click()

username_box = driver.find_element_by_id(id_="username")
username_box.send_keys(email_addr)

password_box = driver.find_element_by_id(id_="password")
password_box.send_keys(password)
password_box.send_keys(Keys.ENTER)

time.sleep(3)
job_list = driver.find_elements_by_class_name(name="jobs-search-results__list-item")
print(len(job_list))

for job in job_list:
    job.click()
    time.sleep(3)
    apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card .artdeco-button__text")

    if apply_button.text == "Easy Apply":
        save_button = driver.find_element_by_class_name(name="jobs-save-button")
        save_button.click()

        time.sleep(1)
        remove_notification = driver.find_element_by_css_selector(".artdeco-toast-item .artdeco-toast-item__dismiss")
        remove_notification.click()
        time.sleep(2)

