from flask import Flask
from app.data_access.dataframes import students_df
from app.repository.students_repository import class_average

app = Flask(__name__)



if __name__ == '__main__':
    print(class_average(students_df))
    app.run(debug=True)
