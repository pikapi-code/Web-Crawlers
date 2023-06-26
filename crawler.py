import requests
from bs4 import BeautifulSoup

url = 'https://pmkisan.gov.in/Rpt_BeneficiaryStatus_pub.aspx'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Extract the available options for the dropdowns
state_dropdown = soup.find("select", id="ContentPlaceHolder1_DropDownState")
state_options = state_dropdown.find_all("option")[1:]  # Exclude the first default option

# Loop through the states
for state_option in state_options:
    state_value = state_option["value"]
    state_name = state_option.text.strip()

    print(state_name)