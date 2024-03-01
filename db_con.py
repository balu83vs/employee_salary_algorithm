from pymongo import MongoClient

# класс взаимодействия с базой данных mongodb
class DbConnector:
    def __init__(self, host='localhost', port=27017, db_name='newdb', collection_name='sample_collection'):
        self.host = host
        self. port = port 
        self.db_name = db_name
        self.collection_name = collection_name

    # установка соединения
    def add_client(self):
        client = MongoClient(host=self.host, port=self.port)    
        return client
    
    # выбор базы данных
    def start_connect(self):
        db = self.add_client()[self.db_name]
        return db
    
    # выбор коллекции
    def choice_collection(self):
        db_collection = self.start_connect()[self.collection_name]
        return db_collection