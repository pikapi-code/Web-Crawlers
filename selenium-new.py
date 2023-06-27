import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the web driver (make sure you have the appropriate driver executable for your browser)
service = Service(executable_path='H:\Projects\Web Crawlers\chrome\chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Navigate to the initial URL
driver.get("https://pmkisan.gov.in/Rpt_BeneficiaryStatus_pub.aspx")

wait = WebDriverWait(driver, 10)

state_dropdown_id = 'ContentPlaceHolder1_DropDownState'
district_dropdown_id = 'ContentPlaceHolder1_DropDownDistrict'
subdistrict_dropdown_id = 'ContentPlaceHolder1_DropDownSubDistrict'
block_dropdown_id = 'ContentPlaceHolder1_DropDownBlock'
village_dropdown_id = 'ContentPlaceHolder1_DropDownDistrictVillage'

# Function to select dropdown values with retry mechanism
def select_dropdown_value(element_id, value):
    attempts = 0
    max_attempts = 100

    while attempts < max_attempts:
        try:
            dropdown_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            dropdown_select = Select(dropdown_element)
            dropdown_select.select_by_visible_text(value)
            for i in dropdown_select.options:
                print(i.text)
            break
        except StaleElementReferenceException:
            attempts += 1

state_value = "DELHI"
select_dropdown_value(state_dropdown_id, state_value)

# Read the dynamically populated dropdown values
district_dropdown = Select(driver.find_element(By.ID, district_dropdown_id))
district_values = [option.text for option in district_dropdown.options][1:]  # Exclude the first empty option

for district_value in district_values:
    select_dropdown_value(district_dropdown_id, district_value)

    subdistrict_dropdown = Select(driver.find_element(By.ID, subdistrict_dropdown_id))
    subdistrict_values = [option.text for option in subdistrict_dropdown.options][1:]

    for subdistrict_value in subdistrict_values:
        select_dropdown_value(subdistrict_dropdown_id, subdistrict_value)
        