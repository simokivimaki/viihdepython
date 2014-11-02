# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parseSchedule():
    schedules = []
    session = requests.Session()
    fromYear = 2009
    tillYear = datetime.today().year
    for year in range(fromYear, tillYear+1):
        schedules.extend(parseYear(session, year))
    print 'Simpsonit.org: Done.'
    return schedules

# Hakee Suomessa esitettyjen Simpsonien aikataulut valitulta vuodelta
def parseYear(session, year):
    schedules = []
    url = 'http://simpsonit.org/jaksot/tv-esitykset-suomessa/' + str(year)
    soup = BeautifulSoup(session.get(url).content)
    for listing_table in soup.find_all('table', class_='tv-archive'):
        for tr in listing_table.find_all('tr'):
            schedules.extend(handle_schedule_tr(tr))
    print 'Simpsonit.org: Found', len(schedules), 'schedules for year', year
    return schedules

def handle_schedule_tr(tr):
    schedules = []
    tds = tr.find_all('td')
    # päivä muodossa 'dd.MM.yyyy'
    date_string = tds[0].string[3:-1]
    for schedule_b in tds[1].find_all('b'):
        time_string = schedule_b.string[:5]
        dt = datetime.strptime(date_string + ' ' + time_string, "%d.%m.%Y %H:%M")
        episode_a = schedule_b.find_next_sibling('a')
        episode_url = episode_a.get('href')
        name = episode_a.string
        m = re.match(r'/jaksot/(\d+)/(\d+)/', episode_url)
        season = int(m.group(1))
        episode = int(m.group(2))
        #print dt, season, episode, name
        schedules.append({'datetime': dt,
                          'season': season,
                          'episode': episode,
                          'name': name})
    return schedules

# for testing
if __name__ == '__main__':
    print parseSchedule()
