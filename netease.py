#coding=utf-8
from api import NetEase
import time
import webbrowser

class RasWxMusicbox:
    def __init__(self, song_name):
        self.mp3_date = None
        netease = NetEase()
        data = netease.search(song_name, stype=1, offset=0, total='true', limit=60)
#        print data
        song_ids = []
        if 'songs' in data['result']:
            if 'mp3Url' in data['result']['songs']:
                songs = data['result']['songs']

            else:
                for i in range(0, len(data['result']['songs']) ):
                    song_ids.append( data['result']['songs'][i]['id'] )
                songs = netease.songs_detail(song_ids)
        self.mp3_data = netease.dig_info(songs, 'songs')   #歌曲信息，album, artist, song_name, mp3_url

    def get_music(self, index):
        return self.mp3_data[index]


    def gen_music_list(self):
        #最多显示10条歌曲信息
        music_list = ''
        total = len(self.mp3_data)
        for i in range(total):
            music_list += '**' + str(i) + '**' + u'专辑：' + self.mp3_data[i]['album_name'] + '\n' \
                        + u'艺术家：' + self.mp3_data[i]['artist'] + '\n' \
                        + u'歌曲名：' + self.mp3_data[i]['song_name'] + '\n' \
                        + '-------------------' + '\n'
        return music_list

    def get_music_url(self, song_id):
        if song_id > 9:
            pass
        try:
            return self.mp3_data[song_id]['mp3_url']
        except:
            pass



'''

        for mp3_url  in mp3_url_data:
            print mp3_url['album_name']
            print mp3_url['artist']
            print mp3_url['song_name']
            print mp3_url['mp3_url']
            print '---------------------------'

'''

if __name__ == '__main__':
    mb = RasWxMusicbox(u'南山南')
    print mb.mp3_data
    print mb.get_music(2)



#    webbrowser.open(mp3_url)
'''
[{'mp3_url': u'http://m2.music.126.net/GkFXC6qt6rEU2q9KYU-6yQ==/1373290025677371.mp3', 
'song_id': 41462137, 'album_name': u'\u6587\u6b66\u8d1d\u94a2\u7434\u6539\u7f16\u4f5c\u54c1\u96c6\uff082015\u5e74\u5168\u96c6\uff09', 
'song_name': u'\u5357\u5c71\u5357-\u6587\u6b66\u8d1d\u94a2\u7434\u7248', 'artist': u'\u6587\u6b66\u8d1d'}]


'''