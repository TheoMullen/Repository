import time
from selenium import webdriver


workable_job_link = "https://apply.workable.com/gohenry/j/F72BCE3FCC/apply/"

first_name = FIRST_NAME
last_name = LAST_NAME
email = EMAIL
headline = HEADLINE
phone = PHONE
address = ADDR
education = {"my_school": {"field": "my_field",
                           "degree": "my_degree",
                           "start": "01/2018",
                           "end": "06/2018"
                           },
             "my_school_2": {"field": "my_field_2",
                             "degree": "my_degree_2",
                             "start": "07/2018",
                             "end": "01/2019"
                             }
             }

experience = {"experience_1": {"title": "job_title",
                            "company": "my_company",
                            "industry": "my_industry",
                            "summary": "description",
                            "start": "02/2019",
                            "end": "12/2020"
                                },
             "experience_2": {"title": "job_title_2",
                            "company": "my_company_2",
                            "industry": "my_industry_2",
                            "summary": "description_2",
                            "start": "01/2021",
                            "end": "05/2022"
                             }
             }

summary= "Personal description"



driver = webdriver.Chrome(executable_path="/Users/theo/Downloads/chromedriver")
driver.get(workable_job_link)
driver.set_window_size(height=800, width=1500)


first_name_box = driver.find_element_by_id(id_="firstname")
first_name_box.send_keys(first_name)
last_name_box = driver.find_element_by_id(id_="lastname")
last_name_box.send_keys(last_name)
email_box = driver.find_element_by_id(id_="email")
email_box.send_keys(email)
headline_box = driver.find_element_by_id(id_="headline")
headline_box.send_keys(headline)
phone_box = driver.find_element_by_name(name="phone")
phone_box.send_keys(phone)
address_box = driver.find_element_by_id(id_="address")
address_box.send_keys(address)


add_buttons = driver.find_elements_by_css_selector("button")
add_education = add_buttons[1]
add_experience = add_buttons[2]

for _ in education.keys():
    time.sleep(0.5)
    add_education.click()

    school = driver.find_element_by_id(id_="school")
    school.send_keys(_)
    field = driver.find_element_by_id(id_="field_of_study")
    field.send_keys(education[_]["field"])
    degree = driver.find_element_by_id(id_="degree")
    degree.send_keys(education[_]["degree"])
    start_date = driver.find_element_by_name(name="start_date")
    start_date.send_keys(education[_]["start"])
    end_date = driver.find_element_by_name(name="end_date")
    end_date.send_keys(education[_]["end"])
    div_buttons = driver.find_elements_by_css_selector("div button")
    for _ in div_buttons:
        if _.text == "Save":
            save_button = _
    save_button.click()


for _ in experience.keys():
    time.sleep(0.5)
    add_experience.click()

    field = driver.find_element_by_id(id_="title")
    field.send_keys(experience[_]["title"])
    degree = driver.find_element_by_id(id_="company")
    degree.send_keys(experience[_]["company"])
    field = driver.find_element_by_id(id_="industry")
    field.send_keys(experience[_]["industry"])
    degree = driver.find_element_by_id(id_="summary")
    degree.send_keys(experience[_]["summary"])
    start_date = driver.find_element_by_name(name="start_date")
    start_date.send_keys(experience[_]["start"])
    start_date = driver.find_element_by_name(name="end_date")
    start_date.send_keys(experience[_]["end"])

    time.sleep(1)

    div_buttons = driver.find_elements_by_css_selector("div button")
    for _ in div_buttons:
        if _.text == "Save":
            save_button = _
    save_button.click()


summary_box = driver.find_element_by_name(name="summary")
summary_box.send_keys(summary)

print("Autofill complete. Check for any remaining fields to fill out.")
