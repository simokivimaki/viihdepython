# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parse():
    session = requests.Session()
    allEpisodes = []
    season = 1
    while True:
        episodes = parseSeason(session, season)
        if episodes:
            print 'Simpsonit.org: Found', len(episodes), 'episodes for season', season
            allEpisodes.extend(episodes)
            season += 1
        else:
            print 'Simpsonit.org: Done.'
            break
    return allEpisodes    

# Hakee kauden jaksojen nimet
def parseSeason(session, season):
    episodes = []
    params = {'kausi': season}
    url = 'http://simpsonit.org'
    soup = BeautifulSoup(session.get(url, params=params).content)
    for episode_li in soup.find(id='contentCenter').find_all('li'):
        episode_names = list(episode_li.a.stripped_strings)
        if len(episode_names) >= 2:
            episode_and_name_fi = episode_names[0]
            name_en = episode_names[1]
            m = re.match(r'(\d+)\.\s*(.*)', episode_and_name_fi)
            if m:
                episode = m.group(1)
                name_fi = m.group(2)
                #print 's' + str(season) + 'e' + episode + ':', name_fi, name_en
                episodes.append({'season': season,
                                 'episode': int(episode),
                                 'name_fi': name_fi,
                                 'name_en': name_en})
    return episodes


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
    params = {'vuosi': year}
    url = 'http://simpsonit.org/?sivu=esitysaikatauluarkisto'
    soup = BeautifulSoup(session.get(url, params=params).content)
    for listing_table in soup.find_all('table', class_='listing'):
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
        season_episode_name = list(schedule_b.find_next_sibling('a').stripped_strings)
        season_episode = season_episode_name[0][:-2]
        name = season_episode_name[1]
        m = re.match(r'(\d+)x(\d+)', season_episode)
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