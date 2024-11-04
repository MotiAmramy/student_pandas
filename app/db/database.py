from pymongo import MongoClient


from app.settings.config import DB_URL


client = MongoClient(DB_URL)


school_db = client['school']


students = school_db['students']
courses = school_db['courses']
chatgpt_users = school_db['chatgpt_users']
avg_collection = school_db['avg_collection']
