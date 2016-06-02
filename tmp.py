#coding=utf-8

import eyed3

mp3 = 'http://m2.music.126.net/GkFXC6qt6rEU2q9KYU-6yQ==/1373290025677371.mp3'
tmp = eyed3.load(mp3)
print tmp.info.time_sec