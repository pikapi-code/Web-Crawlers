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

dropdown_values = {
    "ContentPlaceHolder1_DropDownState": "DELHI",
    'ContentPlaceHolder1_DropDownDistrict': 'CENTRAL',
    'ContentPlaceHolder1_DropDownSubDistrict': 'Civil Lines',
    'ContentPlaceHolder1_DropDownBlock': 'Central (Burari)',
    'ContentPlaceHolder1_DropDownVillage': 'Badar Pur Majra Burari - (63952)'
}

# Function to select dropdown values with retry mechanism
def select_dropdown_value(element_id, value):
    attempts = 0
    max_attempts = 5
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

# Select values for each dropdown using the retry mechanism
for element_id, value in dropdown_values.items():
    select_dropdown_value(element_id, value)

# Click on the "Get Report" button
get_report_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_btnsubmit"))
)
get_report_button.click()

# Wait for the table to load
table_locator = (By.ID, "ContentPlaceHolder1_GridView1")
table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(table_locator)
)

# Scrape table data
all_data = []
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows[1:]:  # Skip the header row
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    all_data.append(row_data)

# Save data to a CSV file
filename = "table_data.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)


#driver.close()