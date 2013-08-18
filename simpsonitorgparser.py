import re
import requests
from bs4 import BeautifulSoup

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

# for testing
if __name__ == '__main__':
    print parse()