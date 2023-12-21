from flask import Flask
from flask import render_template
from flask import request 


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    new_todo = request.form["new_todo"]
    todos_list.append(new_todo)
    return render_template("todo.html.jinja",todos_list=todos_list)

todos_list=['own a popeyes', 'own a kfc']