#!/usr/bin/python
# -*- coding: utf-8 -*-

import elisaviihde


def main():
    e = elisaviihde.Elisaviihde()
    if not e.login():
        return
    
    folder_name = raw_input('Look from folder (enter for all): ')
    if folder_name:
        folder_name = unicode(folder_name, 'utf-8')
        folder = e.find_folder(folder_name)
        if folder:
            folderid = folder['id']
        else:
            print 'Folder', folder_name, 'not found'
            return
    else:
        folderid = ''  # root folder

    recordings = e.ls_recordings_recursive(folderid, [])
    found_duplicates = find_duplicates(e, recordings)
    
    answer = raw_input("Enter 'y' to delete duplicates, anything else to cancel: ")
    if answer == 'y':
        for key, recordings in found_duplicates.iteritems():
            print 'Processing:', key[0], ';', key[1], '; HD', key[2]
            first = True
            for recording in recordings:
                if first:
                    print 'Kept first', recording['start_time'], recording['channel']
                    first = False
                else:
                    status = e.remove(recording['id'])
                    print 'DELETED', status, recording['start_time'], recording['channel']
        print 'Delete duplicates done.'
    else:
        print 'Delete duplicates canceled.'
        
    
def find_duplicates(e, recordings):
    # arrange programs as hastable {(name, short_text, isHD): [recording, recording], ...}
    # (HD recording is considered as different program)
    recordings_dict = {}
    for recording in recordings:
        program = e.get_program_info(recording['program_id'])
        is_hd = 'hd' in program['channel'].lower()
        key = (program['name'].strip(), program['short_text'].strip(), is_hd)
        value = recordings_dict.get(key, [])
        value.append(recording)
        recordings_dict[key] = value
    
    # hastable {(name, short_text, isHD): [recording, recording], ...} where recordings ordered by timestamp
    duplicate_recordings_dict = {}
    for key, recordings in recordings_dict.iteritems():
        if len(recordings) > 1:
            recordings.sort(key=lambda recording: recording['timestamp'])
            duplicate_recordings_dict[key] = recordings
            print 'Found duplicates for:', key[0], ';', key[1], '; HD', key[2]
            for recording in recordings:
                print '*', recording['start_time'], recording['channel']
    print 'Total', len(duplicate_recordings_dict)
    return duplicate_recordings_dict

if __name__ == '__main__':
    main()
