from bs4 import BeautifulSoup
import requests

cz_flight_list = "https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=SHA&c2=SYX&d1=2020-03-07&at=1&ct=0&it=0&b1=SHA-PVG&b2=SYX"

CZ = requests.get(cz_flight_list).content
soup = BeautifulSoup(CZ, "html.parser")
print(soup)
from_to = soup.find_all("div")

for i in from_to:
    print(i)