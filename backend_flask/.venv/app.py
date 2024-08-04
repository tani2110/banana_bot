import chatbot
from flask import Flask , request, jsonify
from flask_cors import CORS
import psycopg2
import json
import re

conn = psycopg2.connect(host="localhost",dbname = "courseweb",user = "postgres",password = "tani123$",port = 5432)
app = Flask(__name__)
CORS(app) 

def is_bitsian(email):
  pattern = r"^f[0-9_+&.-]+@hyderabad+\.bits\-pilani\.ac\.in$"
  return re.match(pattern, email) is not None


def create_db_and_table():
    try:
        conn = psycopg2.connect(host="localhost",dbname = "courseweb",user = "postgres",password = "tani123$",port = 5432)
        cur = conn.cursor()


        users = 'users'
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {users} (
                user_id serial PRIMARY KEY,
                mail VARCHAR(50),
                password varchar(20)
            );
        """
        cur.execute(create_table_query)
        courses = 'courses'
        create_table_courses = f"""
                    CREATE TABLE IF NOT EXISTS {courses} (
                        course_id serial PRIMARY KEY,
                        data VARCHAR(20) NOT NULL
                    );
                """

        cur.execute(create_table_courses)
        conn.commit()

        cur.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while creating database or table:", error)


create_db_and_table()


@app.route('/signup' , methods = ['POST'])
def index():
    if request.method == "POST":
        conn = psycopg2.connect(host="localhost",dbname = "courseweb",user = "postgres",password = "tani123$",port = 5432)
        cur1 = conn.cursor()
        r = request.json
        mail = r['email']
        password = r['pass']
        if is_bitsian(mail):
            cur1.execute("insert into users (mail ,password) values ( %s , %s );" , ( mail, password))
            conn.commit()
            cur1.close()
            conn.close()
            return jsonify({"response": "hi user has been created!"})
        else:
            return jsonify({"response": "Not a bitsian"})


@app.route('/chatbot' , methods = ['POST'])
def prompt():
    if request.method == "POST":
        r = request.json
        input = r['input']
        my_string = chatbot.prompt(input)

        json_data = {"data": my_string}

        json_string = json.dumps(json_data)
        return json_string


if __name__ == "__main__":
    app.run(debug = True , port = 5000)

conn.commit()
conn.close()


