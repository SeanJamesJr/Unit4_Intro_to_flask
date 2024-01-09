from flask import Flask
from flask import render_template
from flask import request 
from flask import redirect
import pymysql

conn = pymysql.connect(
    database ='sjamesjr_todos',
    user='sjamesjr',
    password='250415031',
    host='10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)
app = Flask(__name__)
todos_list=['own a popeyes', 'own a kfc']


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        cursor =conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")
        cursor.close()
        
                
        todos_list.append(new_todo)

    cursor = conn.cursor()
    cursor.execute('SELECT * from `todos`')
    results = cursor.fetchall()
    cursor.close()
    conn.commit()
    return render_template("todo.html.jinja",todos_list=results)


@app.route('/delete_todo/<int:todo_index>',methods=['POST'])
def todo_delete(todo_index):
   cursor = conn.cursor()
   cursor.execute(f"DELETE FROM `todos` WHERE `id`= {todo_index}")
   cursor.close()
   conn.commit()
   return redirect('/')
