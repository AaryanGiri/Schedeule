import requests
import re
from bs4 import BeautifulSoup

url = "https://www.siliconvalleytemple.net/event_calendar.jsp"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
tables = soup.select('div.contents table')

information_list = []

for table in tables:
    rows = table.select('tr')
    for row in rows:
        columns = row.select('td')
        if len(columns) >= 2:
            date = columns[0].get_text(strip=True)
            event = columns[1].get_text(strip=True)

            if event and event[0].isalpha():
                match = re.search(r'\d', event)
                if match:
                    index = match.start()
                    new_string = event[index:]
                    information_list.append((date, new_string))
            else:
                information_list.append((date, event))

# for i in information_list:
#     print(i)

information_dict = []

for date, event in information_list:
    indices1 = []
    indices2 = []

    for i in range(len(event)):
        if event[i] == 'M':
            indices1.append(i)
        if event[i] == ":":
            indices2.append(i)

    for i in indices1:
        for j in indices2:
            if j - i == 1:
                index = j

    time = event[:index]
    event_name = event[index+2:]

    for i in range(len(time)):
        if time[i] == "t":
            ind = i

    start_time = time[:ind-1]
    end_time = time[ind+3:]

    event_dict = {
        'Date': date,
        'Start Time': start_time,
        'End Time': end_time,
        'Event Name': event_name
    }
    information_dict.append(event_dict)

for event in information_dict:
    print(event)
