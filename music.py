import sys
import OutputClass
from music_controller import MusicController
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
        for music in record:
            self.output.print('id', music.id, ' Title:', music.title, '  Artist', music.artist_name, '   Duration', music.duration)

    def searchmusic(self, s):
        record = self.music.search(s)
        count = 0
        for music in record:
            self.output.print('id', music.id, ' Title:', music.title, '  Artist', music.artist_name, '   Duration', music.duration)
            count = count + 1
        if count == 0:
            self.output.print('No matches')

    def extractmusic(self, id):
        music = self.music.get(id)
        self.output.print('id:', music.id)
        self.output.print('title:', music.title)
        self.output.print('Artist:', music.artist_name)
        self.output.print('Duration:', music.duration)
        self.output.print('Lyrics:', music.lyrics)

def main():
    if not Path('musicdb.sqlite').is_file():
        os.system("python ./musicdb.py")

    db = database.Database('musicdb.sqlite')
    outputInstance = OutputClass.Output()
    musicInstance = MusicController(db)
    m1 = App(outputInstance, musicInstance)

    if '-all' in arguments and '-s' not in arguments :
        m1.allmusic()

    elif '-all' in arguments and '-s' in arguments:
        s = sys.argv[2][3:]
        s = str(s)
        s = s.lower()
        m1.searchmusic(s)

    elif '-id' in arguments:
        id = sys.argv[1][4:]
        id = int(id)
        m1.extractmusic(id)
    else:
        print('Check input argument to ensure it conforms with the assigned flag convention')

main()
