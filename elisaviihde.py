import requests
import urllib2
import getpass


class Elisaviihde():
    url = 'http://elisaviihde.fi/etvrecorder/'

    # please call login after init
    def __init__(self):
        self.session = requests.Session()

    def login(self, username=None, password=None):
        if username is None:
            username = raw_input('Elisa Viihde Username: ')
        if password is None:
            password = getpass.getpass('Elisa Viihde Password: ')

        params = {'username': username, 'password': password, 'savelogin': None, 'ajax': True}
        r = self.session.get(Elisaviihde.url + 'login.sl', params=params)
        login_ok = r.text == 'TRUE'
        print 'Elisa Viihde Login', 'OK' if login_ok else 'FAILED'
        return login_ok

    def epg(self):
        # TODO showdate parameter?
        params = {'ajax': True}
        r = self.session.get(Elisaviihde.url + 'epg.sl', params=params)
        programs = r.json()
        return programs
        
    '''
    returns
    {"ready_data":[
      {"folders": [
       {"id":"1831910","name":"Simpsonit","size":"28.02 GB", "has_unwatched":"true", "has_wildcards":"true", "has_pin":"","recordings_count": "35"}
       ...
      ],
      "recordings": [
        {"id":"353350198","program_id":"965921", "folder_id":"","name":"True%20Blood%20(16)","channel":"Yle HD","start_time":"ti 30.07.2013 00:05","timestamp":"2013-07-30T00:05:28+0300","viewcount":"4","length": "51"}
        (where id is programviewid)
        ...
      ]}
    
    ]}
    '''
    def ls(self, folderid=''):
        params = {'folderid': folderid, 'ajax': True}
        r = self.session.get(Elisaviihde.url + 'ready.sl', params=params)
        ready_data = r.json()
        return ready_data
    
    def get_program_info(self, programid):
        params = {'programid': programid, 'ajax': True}
        r = self.session.get(Elisaviihde.url + 'program.sl', params=params)
        program_data = r.json()
        program_data['name'] = unquote(program_data['name'])
        program_data['channel'] = unquote(program_data['channel'])
        program_data['short_text'] = unquote(program_data['short_text'])
        return program_data
    
    def record(self, programid):
        params = {'programid': programid, 'record': programid, 'ajax': True}
        r = self.session.get(Elisaviihde.url + 'program.sl', params=params)
        return r.text
    
    def move(self, programviewid, folderid):
        params = {'move': True, 'programviewid': programviewid, 'destination': folderid, 'ajax': True}
        r = self.session.get(Elisaviihde.url + 'ready.sl', params=params)
        return r.text
    
    def remove(self, programviewid):
        params = {'removep': programviewid, 'ajax': True}
        r = self.session.get(Elisaviihde.url + 'program.sl', params=params)
        return r.text
        
    def create_subfolder(self, foldername, parentid=None):
        params = {'create_subfolder': True, 'folder': foldername, 'parent': parentid, 'ajax': True}
        r = self.session.get(Elisaviihde.url + 'ready.sl', params=params)
        print 'Create subfolder', foldername, r.text
        return self.find_folder(foldername, parentid)

    # Find folder by name from folder (None means root)
    def find_folder(self, foldername, parentid=None):
        ready_data = self.ls(parentid)
        folders = get_folders_from_ready_data(ready_data)
        for folder in folders:
            if folder['name'] == foldername:
                return folder
    
    def find_or_create_subfolder(self, foldername, parentid=None):
        folder = self.find_folder(foldername, parentid)
        if folder is None:
            folder = self.create_subfolder(foldername, parentid)
        return folder
    
    def ls_recordings(self, folderid):
        return get_recordings_from_ready_data(self.ls(folderid))
    
    def ls_recordings_recursive(self, folderid, result):
        ready_data = self.ls(folderid)
        folders = get_folders_from_ready_data(ready_data)
        recordings = get_recordings_from_ready_data(ready_data)
        result.extend(recordings)
        for folder in folders:
            self.ls_recordings_recursive(folder['id'], result)
        return result
        

def get_folders_from_ready_data(ready_data):
    return ready_data['ready_data'][0]['folders']


def get_recordings_from_ready_data(ready_data):
    return ready_data['ready_data'][0]['recordings']


def unquote(text):
    # %-encodings decoded (NB python 2 urllib2 does not support unicode strings)
    return urllib2.unquote(text.encode('ascii')).decode('utf8')
