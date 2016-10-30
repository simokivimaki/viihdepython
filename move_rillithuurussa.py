#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import cli
import elisaviihde
import wikipedia_rillithuurussa_parser
from user_input import get_input


def main():
    parser = cli.init_argparser()
    parser.add_argument('-f', '--folder_name', help='Elisa Viihde Rillit huurussa folder name')
    parser.add_argument('-s', '--season_prefix', help='prefix for season folder name')
    params = parser.parse_args()

    username = cli.read_input(params.user, 'Elisa Viihde Username')
    password = cli.read_password(params.passfile, 'Elisa Viihde Password')

    e = elisaviihde.Elisaviihde()
    if not e.login(username, password):
        return

    folder_name = cli.read_input(params.folder_name,
                                 'Elisa Viihde Rillit huurussa folder name [Rillit huurussa]',
                                 'Rillit huurussa')
    season_folder_name = cli.read_input(params.season_prefix,
                                        'prefix for season folder name or "None" [Season ]',
                                        'Season ')
    if season_folder_name == 'None':
        season_folder_name = u''

    folder = e.find_folder_by_name(folder_name)
    if folder is None:
        print('Folder', folder_name, 'not found')
        return

    episodes = wikipedia_rillithuurussa_parser.parse_episodes()
    folder_id = folder['id']
    root_recordings = e.recordings(folder_id)

    to_be_moved = []  # list of (recording, episode) pairs
    for recording in root_recordings:
        episode = find_episode(episodes, recording)
        if episode:
            to_be_moved.append((recording, episode))
    print('Found', len(to_be_moved), 'episodes to be moved')

    answer = get_input("Enter 'y' to continue, anything else to cancel: ")
    if answer == 'y':
        for move in to_be_moved:
            recording = move[0]
            episode = move[1]
            target_folder = e.find_or_create_subfolder(season_folder_name + str(episode['season']),
                                                       folder_id)
            try:
                status = e.move(recording['programId'], target_folder['id'])
            except TypeError:
                print("Failed to move", recording['programId'])
                continue
            print('MOVED:', status, recording['description'], episode['name_fi'], 'to', target_folder['name'])
        print("Moving done.")
    else:
        print("Moving canceled.")


def find_episode(episodes, recording):
    result = []
    for episode in episodes:
        if recording['name'].startswith('Rillit huurussa') \
                and recording['description'].startswith(episode['name_fi']):
            result.append(episode)

    if len(result) > 1:
        print('SKIPPED: found more than 1 episodes for', recording['description'], result)
    elif len(result) == 1:
        episode = result[0]
        print('MATCH:', recording['description'], '->', 'Season', episode['season'], episode['name_fi'])
        return episode
    else:
        print('SKIPPED: found 0 episodes for', recording['description'])

if __name__ == '__main__':
    main()
