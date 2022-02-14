import psycopg2
from psycopg2.extras import RealDictCursor
import os

class Model():

    def __init__(self):
        self.DATABASE_URL = os.environ['DATABASE_URL']
        self.db = None
        self.cursor = None

    def open_connection(self):
        self.db = psycopg2.connect(self.DATABASE_URL)
        self.cursor = self.db.cursor(cursor_factory=RealDictCursor)
        print("Connection opened...")


    def close_connection(self):
        self.cursor.close()
        self.db.close()
        self.db = None
        self.cursor = None
        print("Connection closed...")

model = Model()