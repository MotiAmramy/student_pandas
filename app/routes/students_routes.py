from flask import Blueprint, jsonify


from app.data_access.dataframes import students_df
from app.repository.students_repository import chat_gpt_users


students_blueprint = Blueprint('students', __name__)


@students_blueprint.route('/chat_users', methods=['GET'])
def chat_users():
   chat_df = chat_gpt_users(students_df, used=True)
   chat_df['_id'] = chat_df['_id'].astype(str)
   return jsonify(chat_df.to_dict(orient="records")), 200


@students_blueprint.route('/non_chat_users', methods=['GET'])
def chat_users():
   chat_df = chat_gpt_users(students_df, used=False)
   chat_df['_id'] = chat_df['_id'].astype(str)
   return jsonify(chat_df.to_dict(orient="records")), 200