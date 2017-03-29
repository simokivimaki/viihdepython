from __future__ import absolute_import, division, print_function, unicode_literals
import requests
import json
import time


class Elisaviihde:
    url = 'https://elisaviihde.fi/'

    # please call login after init
    def __init__(self):
        self.session = requests.Session()

    def login(self, username, password):
        params = {'username': username, 'password': password}
        r = self.session.post(Elisaviihde.url + 'api/user', data=params)
        login_ok = r.status_code == 200
        print('Elisa Viihde Login', 'OK' if login_ok else 'FAILED')
        return login_ok

    ''' (folders contains folders recursively)
depth: 2
folders: []
hasHierarchyRecordingRules: true
hasNewRecordings: true
hasRecordingRules: true
id: 1831964
locked: false
name: "A-studio"
newRecordingsCount: 4
open: false
parentFolder: false
    '''
    def folders(self):
        r = self.session.get(Elisaviihde.url + 'tallenteet/api/folders')
        result = r.json()
        return result['folders']

    ''' (array of recordings)
channel: "Sub"
channelId: 42
description: "Kauhujen talo XXV. Simpsonit sukeltavat toiseen ulottuvuuteen ja kokevat Moen johtaman "Kellopeliappelsiini"-jengin vallan. Amerikkalainen piirrossarja."
duration: 1800
durationMinutes: 30
endTimeUTC: 1429034400000
finished: true
folderId: 1831910
isWatched: true
name: "Simpsonit (12)"
programId: 1902642
recordingId: 0
recordingState: "finished"
scrambled: false
serviceName: "Sub"
startTime: "14.04.2015 20.30"
startTimeFormatted: "ti 14.04.2015 20.30"
startTimeUTC: 1429032600000
thumbnail: "http://thumbs.elisaviihde.fi/thumbnails/1902642.jpg"
thumbnailUrl: "//thumbs.elisaviihde.fi/thumbnails/1902642.jpg"
    '''
    def recordings(self, folderid):
        allresults = []
        page = 0
        while True:
            params = {'page': page, 'sortBy': 'startTime', 'sortOrder': 'desc', 'watchedStatus': 'all'}
            r = self.session.get(Elisaviihde.url + 'tallenteet/api/recordings/' + str(folderid), params=params)
            result = r.json()
            if len(result) == 0:
                break
            allresults.extend(result)
            page += 1
        print('Found', len(allresults), 'recordings for folder', folderid)
        return allresults

    def delete(self, programid):
        r = self.session.delete(Elisaviihde.url + 'tallenteet/api/recordings/' + str(programid))
        result = r.status_code == 200
        print('Deleted recording', programid, ':', result)
        return result

    def create_subfolder(self, foldername, parentid):
        headers = {'Content-Type': 'application/json'}
        data = {'parentId': parentid, 'folderName': foldername}
        folders = self.session.put(Elisaviihde.url + 'tallenteet/api/folder', headers=headers, data=json.dumps(data))
        print('Created folder', foldername)
        return find_folder_recursive(folders, 'name', foldername)

    def move(self, programid, folderid):
        params = {'folderId': folderid}
        r = self.session.put(Elisaviihde.url + 'tallenteet/api/recordings/move/' + str(programid), params=params)
        result = r.status_code == 200
        print('Moved recording', programid, 'to folderid', folderid, ':', result)
        return result

    def find_folder_by_name(self, foldername):
        folders = self.folders()
        return find_folder_recursive(folders, 'name', foldername)

    def find_folder_by_id(self, folderid):
        folders = self.folders()
        return find_folder_recursive(folders, 'id', folderid)
    
    def find_or_create_subfolder(self, foldername, parentid):
        folders = self.find_folder_by_id(parentid)['folders']
        folder = find_folder_recursive(folders, 'name', foldername)
        if folder is None:
            folder = self.create_subfolder(foldername, parentid)
        return folder

    def ls_recordings_recursive(self, folder, result):
        recordings = self.recordings(folder['id'])
        result.extend(recordings)
        subfolders = folder['folders']
        for subfolder in subfolders:
            self.ls_recordings_recursive(subfolder, result)
        return result


def find_folder_recursive(folders, key, value):
    for folder in folders:
        if folder[key] == value:
            return folder
    for folder in folders:
        return find_folder_recursive(folder['folders'], key, value)
    return None
