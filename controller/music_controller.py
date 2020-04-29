from model import database

from model import music_model



class MusicController():
    def __init__(self, db):
        self.db = db
    def get_all(self):
        # return a list of MusicModel instance
        records = self.db.fetch_all("SELECT id, title, artist_name, duration FROM Music")
        result = []
        for record in records:
            model = music_model.MusicModel(record[0], record[1], record[2], record[3])
            result.append(model)
        return result

    def get(self, *s):
        record = self.db.fetch_one("SELECT * FROM Music WHERE id = ?", *s)
        return music_model.MusicModel(record[0], record[1], record[2], record[4], record[3])
    def search(self, s):
        # return a list of MusicModel instance
        params = []
        params.append("%"+s+"%")
        params.append("%"+s+"%")
        records = self.db.fetch_all("SELECT id, title, artist_name, duration FROM Music WHERE title LIKE ? OR artist_name LIKE ? COLLATE NOCASE", *params)
        result = []
        for record in records:
            model = music_model.MusicModel(record[0], record[1], record[2], record[3])
            result.append(model)
        return result