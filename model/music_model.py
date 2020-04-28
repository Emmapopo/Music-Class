from model import database

db = database.Database('musicdb.sqlite')

class MusicModel():

    def get_all(self):
        records = db.execute_all("SELECT id, title, artist_name, duration FROM Music")
        return records

    #id is the id number I want to search by
    def get_one_id(self, id):
        records = db.execute_id("SELECT * FROM Music WHERE id = ?", id)
        return records


    # s is the search parameter
    def search(self, s):
        records = db.execute_search("SELECT id, title, artist_name, duration FROM Music WHERE title LIKE ? OR artist_name LIKE ? COLLATE NOCASE", s)
        return records
