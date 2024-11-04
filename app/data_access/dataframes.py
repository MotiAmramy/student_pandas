import pandas as pd


from app.db.database import students, courses, chatgpt_users

students_df = pd.DataFrame(list(students.find()))
courses_df = pd.DataFrame(list(courses.find()))
chatgpt_users_df = pd.DataFrame(list(chatgpt_users.find()))



