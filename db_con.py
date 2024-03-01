from pymongo import MongoClient

# класс взаимодействия с базой данных mongodb
class DbConnector:
    def __init__(self, host='localhost', port=27017, 
                 db_name='newdb', collection_name='sample_collection'):
        self._host = host
        self._port = port 
        self._db_name = db_name
        self._collection_name = collection_name

    # установка соединения (подключение клиента)
    def add_client(self):
        client = MongoClient(host=self._host, port=self._port)    
        return client
    
    # выбор базы данных (подключение БД)
    def start_connect(self):
        db = self.add_client()[self._db_name]
        return db
    
    # выбор коллекции (выбор необходимой коллекции)
    def choice_collection(self):
        db_collection = self.start_connect()[self._collection_name]
        return db_collection