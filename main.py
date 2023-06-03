import requests
from bs4 import BeautifulSoup

url = "https://www.siliconvalleytemple.net/event_calendar.jsp"

r = requests.get(url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

tables = soup.select('div.contents table')

information_list = []

for table in tables:
    rows = table.select('tr')
    for row in rows:
        columns = row.select('td')
        if len(columns) >= 2:
            date = columns[0].get_text(strip=True)
            event = columns[1].get_text(strip=True)

            information_list.append((date, event))

for item in information_list:
    print(item)

