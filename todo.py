from flask import Flask
from flask import render_template
from flask import request 
from flask import redirect
import pymysql

conn = pymysql.connect(
 database ='todos',
    user='sjamesjr_todos',
    password='250415031',
    host='10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)
app = Flask(__name__)
todos_list=['own a popeyes', 'own a kfc']


@app.route("/", methods=['GET','POST'])
def index():

    conn = pymysql.connect(
    database ='world',
    user='sjamesjr',
    password='250415031',
    host='10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)

    cursor = conn.cursor()
    cursor.execute('SELECT `description, from `todos`')
    results = cursor.fetchall()
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        todos_list.append(new_todo)
    
    return render_template("todo.html.jinja",todos_list=results)


@app.route('/delete_todo/<int:todo_index>',methods=['POST'])
def todo_delete(todo_index):
   del todos_list[todo_index]
   return redirect('/')
