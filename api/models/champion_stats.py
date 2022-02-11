import mysql.connector
from .base import model

class Stats():

    def __init__(self):
        self.champ_id = None
        self.champ_stars = None
        self.champ_rank = None
        self.champ_prestige = None
        self.champ_HP = None
        self.champ_attack = None
        self.champ_crit_rate = None
        self.champ_crit_damage = None
        self.champ_armor = None
        self.champ_block_proficiency = None
        self.champ_energy_resist = None
        self.champ_physical_resist = None
        self.champ_crit_resist = None

    def read_champ_stats(self, name, stars, rank):

        model.open_connection()
        query = "SELECT champ_id from champions WHERE champ_name = %s"
        model.cursor.execute(query, (name,))
        self.champ_id = model.cursor.fetchone()['champ_id']
        model.close_connection()

        model.open_connection()
        query = "SELECT * FROM champ_stats WHERE champ_id = %s AND champ_stars = %s AND champ_rank = %s"
        model.cursor.execute(query, (self.champ_id, stars, rank))
        champ_stats = model.cursor.fetchall()
        model.close_connection()

        return champ_stats

    
    def create_champ_stats(self, name):

        model.open_connection()
        query = "SELECT champ_id FROM champions WHERE champ_name = %s"
        model.cursor.execute(query, (name,))
        self.champ_id = model.cursor.fetchone()['champ_id']
        model.close_connection()

        upload_stats = [
            self.champ_id,
            self.champ_stars,
            self.champ_rank,
            self.champ_prestige,
            self.champ_HP,
            self.champ_attack,
            self.champ_crit_rate,
            self.champ_crit_damage,
            self.champ_armor,
            self.champ_block_proficiency,
            self.champ_energy_resist,
            self.champ_physical_resist,
            self.champ_crit_resist, 
        ]

        model.open_connection()
        query = "INSERT INTO champ_stats VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        model.cursor.execute(query, (upload_stats))
        model.db.commit()
        model.close_connection()