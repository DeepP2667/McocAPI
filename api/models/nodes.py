import psycopg2
from ..models.base import model

class Nodes():

    def __init__(self):
        self.node_id = None
        self.node_name = None
        self.node_info = None

    
    def create_node(self):

        model.open_connection()
        query = "INSERT INTO nodes(node_name, node_info) VALUES(%s, %s)"
        model.cursor.execute(query, (self.node_name, self.node_info))
        model.db.commit()
        model.close_connection()

    @staticmethod
    def read_nodes():

        model.open_connection()
        query = "SELECT * FROM nodes"
        model.cursor.execute(query)
        nodes = model.cursor.fetchall()
        model.close_connection()

        return nodes