import xbmc
from kodi_six import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs
#from xbmc import Plugin, xbmcgui
#from xbmcswift2 import Plugin, xbmcgui
from kodi_six import Plugin
from resources.lib import criminalpodcast
from xmbc import xmbcplugin

#URL = "http://feeds.thisiscriminal.com/CriminalShow"
URL = "https://feeds.soundcloud.com/users/soundcloud:users:69651204/sounds.rss"
plugin = Plugin()

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "resources/media/icon.jpg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.criminalpodcast/resources/media/icon.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('new_to_criminal'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.criminalpodcast/resources/media/cropped-favicon-2-180x180-inverted.png"},
    ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = criminalpodcast.get_soup(URL)
    playable_podcast = criminalpodcast.get_playable_podcast(soup)
    items = criminalpodcast.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = criminalpodcast.get_soup(URL)
    playable_podcast1 = criminalpodcast.get_playable_podcast1(soup)
    items = criminalpodcast.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/new_to_criminal/')
def new_to_criminal():
    #soup = criminalpodcast.compile_new_to_criminal(URL)
    compile_ntc = criminalpodcast.get_new_to_criminal
    items = criminalpodcast.compile_new_to_criminal(compile_ntc)
    return items

if __name__ == '__main__':
    plugin.run()
