import mysql.connector
from .base import model

class Champions():

    def __init__(self):
        self.champ_name = None
        self.champ_class = None
        self.offense_rank = None
        self.defense_rank = None

    @staticmethod
    def read_all_champs():
        model.open_connection()

        query = "SELECT champ_name, champ_class, offense_rank, defense_rank FROM champions"
        model.cursor.execute(query)
        stored_champs = model.cursor.fetchall()

        model.close_connection()
        
        return stored_champs

    def create_one_champ(self):

        model.open_connection()
        
        query = "ALTER TABLE champions AUTO_INCREMENT=1"
        model.cursor.execute(query)
        model.db.commit()

        query = "INSERT INTO champions(champ_name, champ_class, offense_rank, defense_rank) VALUES(%s, NULL, NULL, NULL)"
        model.cursor.execute(query, (self.champ_name,))
        model.db.commit()
        
        model.close_connection()





