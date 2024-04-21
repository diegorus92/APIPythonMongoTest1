from pymongo import MongoClient

class Database:
    def __init__(self):
        self._db = self._get_contacts1_database(self._connect_database())

    def _connect_database(self):
        connection = MongoClient('localhost', 27017)
        return connection

    def _get_contacts1_database(self, connection):
        database = connection.contacts1
        return database

    def get_database_context(self):
        return self._db



