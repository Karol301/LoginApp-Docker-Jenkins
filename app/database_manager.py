from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
 
class DatabaseManager:
    def __init__(self):
        mongo_user = os.getenv('MONGO_USER')
        mongo_password = os.getenv('MONGO_PASSWORD')
        mongo_host = "mongo-database" 
        mongo_port = os.getenv('MONGO_PORT', 27017) 
        mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/"

        self.client = MongoClient(mongo_uri)

        self.db = self.client['admin']  
        self.users = self.db.users  

    def user_exists(self, login, password):
        return self.users.find_one({"login": login, "password": password}) is not None

    def add_user(self, login, password):
        self.users.insert_one({"login": login, "password": password})

    def close(self):
        self.client.close()
