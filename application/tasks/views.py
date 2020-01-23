from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Animal

@app.route("/tasks/", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", animals = Animal.query.all())

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html")

@app.route("/tasks/food/") 
def tasks_add_food():
    return render_template("tasks/food.html")

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    #print(request.form.get("name"))
    t = Animal(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))