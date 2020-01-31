from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.tasks.models import Animal
from application.auth.models import User
from application.tasks.forms import AnimalForm

@app.route("/tasks/", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", animals = Animal.query.all())


@app.route("/tasks/<animal_id>/", methods=["GET"]) 
def tasks_show_animal(animal_id):    
    return render_template("tasks/show.html", animal = Animal.query.get(animal_id))


@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = AnimalForm())

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = AnimalForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)


    animal = Animal(form.name.data)
    animal.account_id = current_user.id 

    db.session().add(animal)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))