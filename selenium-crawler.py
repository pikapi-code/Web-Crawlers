from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the web driver (make sure you have the appropriate driver executable for your browser)
service = Service(executable_path='H:\Projects\Web Crawlers\chrome\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigate to the initial URL
driver.get("https://pmkisan.gov.in/Rpt_BeneficiaryStatus_pub.aspx")

wait = WebDriverWait(driver, 10)

state_dropdown_id = 'ctl00$ContentPlaceHolder1$DropDownState'
district_dropdown_id = 'ctl00$ContentPlaceHolder1$DropDownDistrict'
subdistrict_dropdown_id = 'ctl00$ContentPlaceHolder1$DropDownSubDistrict'
block_dropdown_id = 'ctl00$ContentPlaceHolder1$DropDownBlock'
village_dropdown_id = 'ctl00$ContentPlaceHolder1$DropDownVillage'


state_dropdown = Select(driver.find_element(By.NAME, state_dropdown_id))  # Replace with the actual state dropdown ID
state_dropdown.select_by_value(str(7))
time.sleep(5)

district_dropdown = Select(driver.find_element(By.NAME, district_dropdown_id))  # Replace with the actual state dropdown ID

for district_option in district_dropdown.options:
    district_dropdown.select_by_value(district_option.get_attribute('value'))

    subdistrict_dropdown = Select(driver.find_element(By.NAME, subdistrict_dropdown_id))  # Replace with the actual state dropdown ID

    for subdistrict_option in subdistrict_dropdown.options:
        subdistrict_dropdown.select_by_value(subdistrict_option.get_attribute('value'))

        block_dropdown = Select(driver.find_element(By.NAME, block_dropdown_id))  # Replace with the actual state dropdown ID

        for block_option in block_dropdown.options:
            block_dropdown.select_by_value(block_option.get_attribute('value'))
            
            village_dropdown = Select(driver.find_element(By.NAME, village_dropdown_id))  # Replace with the actual state dropdown ID

            for village_option in village_dropdown.options:
                village_dropdown.select_by_value(village_option.get_attribute('value'))
                
                
# Close the browser
driver.quit()
