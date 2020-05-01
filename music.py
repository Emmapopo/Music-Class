from  flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
import sys
import OutputClass
from controller import music_controller
from pathlib import Path
import os
from model import database
import json
from json import dumps

arguments =  str(sys.argv)

class App:
    def __init__(self, outputInstance, musicController):
        self.output = outputInstance
        self.music = musicController

    def allmusic(self):
        record = self.music.get_all()
        result = map(lambda x: x.__dict__, record) 
        return list(result) 
           

    def searchmusic(self, s):
        record = self.music.search(s) 
        result = map(lambda x: x.__dict__, record) 
        return list(result) 

    def extractmusic(self, id):
        music = self.music.get(id)
        return music.__dict__
       


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
    return jsonify({"status":"success","data": all})

@app.route('/musics/<music_id>')
def getone(music_id):
    one = m1.extractmusic(music_id)
    return jsonify({"status":"success","data": one})

@app.route('/musics/search')
def getsearched():
    search_term = request.args.get('q')
    ser = m1.searchmusic(search_term)
    return jsonify({"status":"success","data": ser})


if __name__ == '__main__':
    app.run(debug=True)


