import requests
from bs4  import BeautifulSoup

req = requests.get('https://hackevents.co/hackathons')
soup = BeautifulSoup(req.text, 'lxml')

hack = soup.find_all('div', {'class': 'hackathon'})

print("{:<5} {:<15}: {:<90} : {}, {}\n".format('Sr.No.', 'Date', 'Name of Hackathon', 'City', 'Country'))

for i, f in enumerate(hack, 1):
    month = f.find('div', {'class': 'date'}).find('div', {'class': 'date-month'}).text.strip()
    day_num = f.find('div', {'class': 'date'}).find('div', {'class': 'date-day-number'}).text.strip()
    week_day = f.find('div', {'class': 'date'}).find('div', {'class': 'date-week-days'}).text.strip()

    display = "{} {} {} ".format(day_num, week_day, month)

    name = f.find('div', {'class': 'info'}).find('h2').text.strip()

    city = f.find('div', {'class': 'info'}).find('p').find('span', {'class': 'city'}).text.strip()
    country = f.find('div', {'class': 'info'}).find('p').find('span', {'class': 'country'}).text.strip()

    print("{:<5} {:<15} : {:<90} : {}, {}\n".format(str(i)+')', display, name.title(), city, country))
