#!/usr/bin/python
#coding=utf-8
import time
import itchat
import netease
import threading
import os
import subprocess
import webbrowser
import signal

itchat.auto_login()
will_play_list = []
process = None


def musicbox():
    @itchat.msg_register
    def simple_reply(msg):
        if msg.get('Type', '') == 'Text':
            #return 'I received: %s'%msg.get('Content', '')
            content = msg.get('Content', '')
            key_word = content[0]
            
            #查询待播放列表
            if key_word == 'R':
                all_music_str = ''
                if len(will_play_list) == 0:
                    all_music_str = u'播放列表空'
                else:
                    i = 0
                    for song in will_play_list:
                        all_music_str += str(i) + ' ' + song['song_name'] + '\n'
                        i += 1
                return all_music_str
            #下一曲
            elif key_word == 'N':
                if len(will_play_list) > 0:
                    message = play()
                    del will_play_list[0]
                    return message
                else:
                    return u'播放列表空'
            # 查询
            elif key_word == 'S':
                content_list = content.split()
                song_name = content_list[1]
                musicbox = netease.RasWxMusicbox(song_name)

                if len(content_list) == 2:
                    music_list = musicbox.gen_music_list()
                    return music_list
                if len(content_list) == 3:
                    music_index = int(content_list[2])
                    music_info = musicbox.get_music(music_index)
                    if will_play_list:
                        play()
                        return u'正在播放%s' % song_name
                    else:
                        will_play_list.append(music_info)
                        return u'添加' + music_info['song_name'] + u'成功'
        else:
            pass
    itchat.run()

def play():
    if len(will_play_list) == 0:
        return u'播放列表空'
    else:
        song = will_play_list[0]
        song_name = song['song_name']
        mp3_url = song['mp3_url']
        try:
            subprocess.Popen(['pkill', 'mpg123'])
            time.sleep(.3)
        except:
            pass
        finally:
#            subprocess.Popen(['mpg123', mp3_url])
            webbrowser.open(mp3_url)
        return u'正在播放 %s' % song_name

if __name__ == '__main__':
    musicbox()

