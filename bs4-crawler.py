import requests
from bs4 import BeautifulSoup

url = 'https://pmkisan.gov.in/Rpt_BeneficiaryStatus_pub.aspx'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup)
