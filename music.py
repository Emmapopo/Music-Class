from  flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import sys
import OutputClass
from controller import music_controller
from pathlib import Path
import os
from model import database

arguments =  str(sys.argv)

class App:
    def __init__(self, outputInstance, musicController):
        self.output = outputInstance
        self.music = musicController

    def allmusic(self):
        record = self.music.get_all()
        dict = {}
        for music in record:
            dict.update({music.id:{'Title':music.title, 'Artist': music.artist_name, 'Duration':music.duration }})
        return dict
           

    def searchmusic(self, s):
        record = self.music.search(s) 
        dict = {}
        for music in record:
             dict.update({music.id:{'Title':music.title, 'Artist': music.artist_name, 'Duration':music.duration }})
        return dict

    def extractmusic(self, id):
        dict={}
        music = self.music.get(id)
        dict.update({music.id:{'Title':music.title, 'Artist': music.artist_name, 'Duration':music.duration , 'Lyrics': music.lyrics}})
        return dict
       


if not Path('musicdb.sqlite').is_file():
    os.system("python ./musicdb.py")

db = database.Database('musicdb.sqlite')
outputInstance = OutputClass.Output()
musicInstance = music_controller.MusicController(db)
m1 = App(outputInstance, musicInstance)

app = Flask(__name__)
api = Api(app)


@app.route('/musics/')
def get():
    all = m1.allmusic()
    return jsonify(all)

@app.route('/musics/<music_id>')
def getone(music_id):
    one = m1.extractmusic(music_id)
    return jsonify(one)

@app.route('/musics/q=<search_term>')
def getsearched(search_term):
    ser = m1.searchmusic(search_term)
    return jsonify(ser)


if __name__ == '__main__':
    app.run(debug=True)


