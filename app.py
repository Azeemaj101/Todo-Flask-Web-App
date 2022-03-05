from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Projects/Web Projects/Web-Projects/Flask/todo/todo.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title} - {self.desc} -{self.date_created}"


# @app.route("/a", methods=['GET','POST'])
# def FrontPage():
#     if request.method=="POST":
#         todo = Todo(title=request.form['title'], desc=request.form['desc'])
#         db.session.add(todo)
#         db.session.commit()
    
#     allTodo = Todo.query.all()
#     return render_template('index.html', allTodo = allTodo)

@app.route("/")
def Front():
    return "<h1>Helo</h1>"

# @app.route("/update", methods=['GET','POST'])
# def update():
#     if request.method=="POST":
#         todo = Todo.query.filter_by(sno=request.form['sno1']).first()
#         todo.title = request.form['title1']
#         todo.desc = request.form['desc1']
#         db.session.add(todo)
#         db.session.commit()
#     return redirect("/")


# @app.route("/delete/<int:sno>")
# def delete(sno):
#     todo = Todo.query.filter_by(sno=sno).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port="8000")