

class MusicModel():
    def __init__(self, id = None, title = None, artist_name = None, duration = None, lyrics = None):
        self.id = id
        self.title = title
        self.artist_name = artist_name
        self.duration = duration
        self.lyrics = lyrics

    # def get_all(self):
    #     records = db.fetch_all("SELECT id, title, artist_name, duration FROM Music")
    #     return records

    # #id is the id number I want to search by
    # def get(self, id):
    #     record = db.fetch_one("SELECT * FROM Music WHERE id = ?", self.id)
    #     self.title = record[1]
    #     self.artist_name = record[2]
    #     self.lyrics = record[3]
    #     self.duration = record[4]


    # # s is the search parameter
    # def search(self, s):
    #     records = db.fetch_all("SELECT id, title, artist_name, duration FROM Music WHERE title LIKE ? OR artist_name LIKE ? COLLATE NOCASE", "%"+s+"%", "%"+s+"%")
    #     return records
