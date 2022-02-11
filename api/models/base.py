import mysql.connector
from data_base_config import config

class Model():

    def __init__(self):
        self.db = None
        self.cursor = None

    def open_connection(self):
        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor(dictionary=True)
        print("Connection opened...")


    def close_connection(self):
        self.cursor.close()
        self.db.close()
        self.db = None
        self.cursor = None
        print("Connection closed...")

model = Model()