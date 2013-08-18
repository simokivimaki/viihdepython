#!/usr/bin/python
# -*- coding: utf-8 -*-

import elisaviihde
import simpsonitorgparser

def main():
    
    e = elisaviihde.Elisaviihde()
    if not e.login():
        return
    
    folder_name = raw_input('Elisa Viihde Simpsonit folder name [Simpsonit]: ')
    if not folder_name:
        folder_name = 'Simpsonit'

    simpsonit_folder = e.find_folder(folder_name)
    if simpsonit_folder is None:
        print 'Folder', folder_name, 'not found'
        return
    
    episodes = simpsonitorgparser.parse()
    simpsonit_folder_id = simpsonit_folder['id']
    root_simponit_recordings = e.ls_recordings(simpsonit_folder_id)
    
    to_be_moved = [] # list of (recording, episode) pairs
    for recording in root_simponit_recordings:
        program = e.get_program_info(recording['program_id'])
        episode = find_episode(episodes, program)
        if episode:
            to_be_moved.append((recording, episode))
    print 'Found', len(to_be_moved), 'episodes to be moved'

    answer = raw_input("Enter 'y' to continue, anything else to cancel: ")
    if answer == 'y':
        for move in to_be_moved:
            recording = move[0]
            episode = move[1]
            target_folder = e.find_or_create_subfolder('Season ' + str(episode['season']),
                                                       simpsonit_folder_id)
            status = e.move(recording['id'], target_folder['id'])
            print 'MOVED:', status, recording['start_time'], episode['name_fi'], 'to', target_folder['name']
        print "Moving done."
    else:
        print "Moving canceled."
        
    
def find_episode(episodes, program):
    short_text = program['short_text']
    short_text_canonical = short_text.lower().replace(' -', ',') # fix for "Bart - luottohenkilö"
    result = []
    for episode in episodes:
        if short_text_canonical.startswith(episode['name_fi'].lower()):
            result.append(episode)
    if len(result) > 1:
        print 'SKIPPED: found more than 1 episodes for', short_text, result
    elif len(result) == 1:
        episode = result[0]
        print 'MATCH:', program['start_time'], episode['name_fi'], '->', 'Season', episode['season']
        return episode
    else:
        print 'SKIPPED: found 0 episodes for', short_text, program['id']

if __name__ == '__main__':
    main()