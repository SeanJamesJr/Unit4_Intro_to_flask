from flask import Flask
from flask import render_template
from flask import request 
from flask import redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

conn = pymysql.connect(
    database ='sjamesjr_todos',
    user='sjamesjr',
    password='250415031',
    host='10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)
app = Flask(__name__)
auth= HTTPBasicAuth()
todos_list=['own a popeyes', 'own a kfc']

users = {
    "sean": generate_password_hash("hello"),
    "james": generate_password_hash("popeyes")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route("/", methods=['GET','POST'])
@auth. login_required
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        cursor =conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")
        cursor.close()
        conn.commit()
                
        todos_list.append(new_todo)

    cursor = conn.cursor()
    cursor.execute('SELECT * from `todos` ORDER BY `complete`')
    results = cursor.fetchall()
    cursor.close()
    return render_template("todo.html.jinja",todos_list=results)


@app.route('/delete_todo/<int:todo_index>',methods=['POST'])
def todo_delete(todo_index):
   cursor = conn.cursor()
   cursor.execute(f"DELETE FROM `todos` WHERE `id`= {todo_index}")
   cursor.close()
   conn.commit()
   return redirect('/')

@app.route('/complete_todo/<int:todo_index>',methods=['POST'])
def todo_complete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE`todos` SET `complete`= 1 WHERE  `id` = {todo_index}")
    cursor.close()
    conn.commit()
    return redirect('/')

