import psycopg2
from .base import model

class Champions():

    def __init__(self):
        self.champ_name = None
        self.champ_class = None
        self.offense_rank = None
        self.defense_rank = None

    def read_base_champ_stats(self, name):
        
        model.open_connection()
        query = "SELECT * FROM champions WHERE champ_name = %s"
        model.cursor.execute(query, (name,))
        stored_champs = model.cursor.fetchall()
        model.close_connection()
        
        return stored_champs


    def create_one_champ(self):

        model.open_connection()
        query = "INSERT INTO champions(champ_name, champ_class, offense_rank, defense_rank) VALUES(%s, NULL, NULL, NULL)"
        model.cursor.execute(query, (self.champ_name,))
        model.db.commit()
        model.close_connection()





