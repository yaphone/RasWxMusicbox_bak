#coding=utf-8

import time
import itchat
import netease

itchat.auto_login()

will_play_list = []

def musicbox():
    @itchat.msg_register
    def simple_reply(msg):
        if msg.get('Type', '') == 'Text':
            #return 'I received: %s'%msg.get('Content', '')
            content = msg.get('Content', '')
            if content == 'R':
                all_music_str = ''
                if len(will_play_list) == 0:
                    all_music_str = u'播放列表空' 
                for song in will_play_list:
                    all_music_str += song['song_name'] + '\n'
                return all_music_str
            if content == 'N':
                if len(will_play_list) > 1:
                    will_play_list.pop()
                    return u'正在播放' + will_play_list[0]['song_name']
                else:
                    return u'播放列表空'
            else:
                musicbox = netease.RasWxMusicbox()
                music_info = musicbox.get_music(content)
                will_play_list.append(music_info)
                return u'添加' + content + u'成功'
                
                
        else:
            pass
        
    



    itchat.run()


if __name__ == '__main__':
    musicbox()
    #complex_reply()
