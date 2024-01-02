from flask import Flask
from flask import render_template
from flask import request 
from flask import redirect



app = Flask(__name__)
todos_list=['own a popeyes', 'own a kfc']

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        todos_list.append(new_todo)
    
    return render_template("todo.html.jinja",todos_list=todos_list)


@app.route('/delete_todo/<int:todo_index>',methods=['POST'])
def todo_delete(todo_index):
   del todos_list[todo_index]
   return redirect('/')
