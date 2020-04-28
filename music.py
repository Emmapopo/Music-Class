import sys
import OutputClass
from model import music_model

arguments =  str(sys.argv)
class Music:
    def __init__(self, outputInstance, musicInstance):
        self.output = outputInstance
        self.music = musicInstance

    def allmusic(self):
        record = self.music.get_all()
        for row in record:
            self.output.print('id', row[0], ' Title:', row[1], '  Artist', row[2], '   Duration', row[3])

    def searchmusic(self, s):
        record = self.music.search(s)
        count = 0
        for row in record:
            self.output.print('id', row[0], ' Title:', row[1], '  Artist', row[2], '   Duration', row[3])
            count = count + 1
        if count == 0:
            self.output.print('No matches')

    def extractmusic(self, id):
        record = self.music.get_one_id(id)
        self.output.print('id:', record[0])
        self.output.print('title:', record[1])
        self.output.print('Artist:', record[2])
        self.output.print('Duration:', record[4])
        self.output.print('Lyrics:', record[3])


outputInstance = OutputClass.Output()
musicInstance = music_model.MusicModel()
m1 = Music(outputInstance, musicInstance)

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
