#!/usr/bin/python
# -*- coding: utf-8 -*-

import elisaviihde


def main():
    e = elisaviihde.Elisaviihde()
    parser = e.argparser()
    parser.add_argument('-f', '--folder_name')
    parser.add_argument('-m', '--max_auto_delete')
    params = parser.parse_args()
    if not e.login(params):
        return
          
    folder_name = params.folder_name
    if folder_name is None:
        folder_name = raw_input('Look from folder (enter for all): ')
    if folder_name:
        folder_name = unicode(folder_name, 'utf-8')
        folder = e.find_folder_by_name(folder_name)
        if folder is None:
            print 'Folder', folder_name, 'not found'
            return
    else:
        folder = e.find_folder_by_id(0)

    recordings = e.ls_recordings_recursive(folder, [])
    found_duplicates = find_duplicates(e, recordings)
    
    answer = 'n'
    if params.max_auto_delete is not None:
        if len(found_duplicates) <= int(params.max_auto_delete):
            answer = 'y'
    elif len(found_duplicates) > 0:
        answer = raw_input("Enter 'y' to delete duplicates, anything else to cancel: ")
    
    if answer == 'y':
        for key, recordings in found_duplicates.iteritems():
            print 'Processing:', key[0], ';', key[1]
            first = True
            for recording in recordings:
                if first:
                    print 'Kept first', recording['startTime'], recording['channel']
                    first = False
                else:
                    status = e.delete(recording['programId'])
                    print 'DELETED', status, recording['startTime'], recording['channel']
        print 'Delete duplicates done.'
    else:
        print 'Delete duplicates canceled.'
        exit(-1)
        
    
def find_duplicates(e, recordings):
    # arrange programs as hastable {(name, description): [recording, recording], ...}
    recordings_dict = {}
    for recording in recordings:
        key = (recording['name'].strip(), recording.get('description', '').strip())
        value = recordings_dict.get(key, [])
        value.append(recording)
        recordings_dict[key] = value
    
    # hastable {(name, description): [recording, recording], ...}
    # where recordings ordered by not-HD, startTimeUTC timestamp
    duplicate_recordings_dict = {}
    for key, recordings in recordings_dict.iteritems():
        if len(recordings) > 1:
            recordings.sort(key=lambda recording: (not recording['channel'].endswith('HD'), recording['startTimeUTC']))
            duplicate_recordings_dict[key] = recordings
            print 'Found duplicates for:', key[0], ';', key[1]
            for recording in recordings:
                print '*', recording['startTime'], recording['channel']
    print 'Total', len(duplicate_recordings_dict)
    return duplicate_recordings_dict

if __name__ == '__main__':
    main()
