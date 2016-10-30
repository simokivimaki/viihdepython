# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import re
import requests
from bs4 import BeautifulSoup


def parse_episodes():
    url = 'https://fi.wikipedia.org/wiki/Luettelo_televisiosarjan_Rillit_huurussa_jaksoista'
    episodes = []

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    headline_tags = soup.find_all('span',
                                 class_='mw-headline',
                                 string=re.compile(r'\d+\. tuotantokausi'))

    for headline_tag in headline_tags:
        m = re.match(r'(\d+)', headline_tag.string)
        season = int(m.group(1))
        table_tag = headline_tag.parent.find_next_sibling('table')
        for tr_tag in table_tag.find_all('tr'):
            td_tags = tr_tag.find_all('td')
            if len(td_tags) >= 4:
                episode_number = int(td_tags[1].string)
                name_fi = td_tags[3].string
                episode = {'season': season, 'episode': episode_number, 'name_fi': name_fi}
                #print(episode)
                episodes.append(episode)

    print('Parsing wikipedia Rillit huurussa done')
    return episodes

# for testing
if __name__ == '__main__':
    for episode in parse_episodes():
        print('S{}E{} {}'.format(episode['season'], episode['episode'], episode['name_fi']))
