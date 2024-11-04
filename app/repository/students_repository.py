from datetime import datetime

from pandas import DataFrame

from app.db.database import chatgpt_users, avg_collection


def chat_gpt_users(df: DataFrame, used: bool):
   clean_df = df.dropna(subset=['Uses_ChatGPT'])
   all_gpt_users = clean_df[clean_df['Uses_ChatGPT'] == used]
   return all_gpt_users



def class_average(df: DataFrame):
    clean_df = df.dropna(subset=['Class_Average'])
    avg = clean_df['Class_Average'].mean()
    data = {
       "time": f"{datetime.now()}",
       "avg": f"{avg}"
    }
    # avg_collection.insert_one(data)
    print(list(avg_collection.find()))
    return data