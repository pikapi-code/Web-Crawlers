import requests
from bs4 import BeautifulSoup

url = 'https://pmkisan.gov.in/Rpt_BeneficiaryStatus_pub.aspx'
page = requests.get(url).text

payload = {'ContentPlaceHolder1_DropDownState': 'DELHI', 'ContentPlaceHolder1_DropDownDistrict': 'CENTRAL', 
           'ContentPlaceHolder1_DropDownSubDistrict': 'Civil Lines', 'ContentPlaceHolder1_DropDownBlock': 'Central (Burari)',
           'ContentPlaceHolder1_DropDownVillage': 'Badar Pur Marja Burari - (63952)'}
r = requests.post(url, data=payload)
print(r.status_code)