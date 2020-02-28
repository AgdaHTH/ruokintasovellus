from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.animals.models import Animal
from application.animals.models import Food
from application.auth.models import User
from application.animals.forms import AnimalForm
from application.foods.forms import FoodForm, PriceForm
from application.auth.forms import UserForm

@app.route("/foods/newfood/", methods=["POST"])
def add_food():
    form = FoodForm(request.form)
    
    if not form.validate():
        return render_template("foods/newfood.html", form = form)
   
    food = Food(form.name.data)
    allfoods = Food.query.all()
    loytyiko = 1
    for oldfood in allfoods:
        if oldfood.name == food.name:
            loytyiko = 2

    if loytyiko == 2:
        return render_template("foods/newfood.html", form = form, error = "Food already exists")

    db.session().add(food)
    db.session().commit()

    return redirect(url_for("animals_index"))

@app.route("/foods/newfood/", methods=["GET"])
def new_food_form():
    return render_template("foods/newfood.html", form = FoodForm())

@app.route("/foods/showfood/<food_id>")
def show_food(food_id):    
    return render_template("foods/showfood.html", food = Food.query.get(food_id))

@app.route("/foods/updatefood/<food_id>")
def show_update_food(food_id):
    form = PriceForm(request.form)
    return render_template("foods/updatefood.html", food = Food.query.get(food_id), form=form)

@app.route("/foods/updatefood/<food_id>/", methods=["POST"])
def update_food(food_id):
    form = PriceForm(request.form)

    if not form.validate():
        return render_template("foods/updatefood.html", form = form, food = Food.query.get(food_id))

    newprice = form.price.data
    Food.set_price(food_id, newprice)
    
    db.session().commit()

    food = Food.query.get(food_id)
    return redirect(url_for("show_food", food_id=food.id))

@app.route("/foods/food/delete/<food_id>")
def foods_delete(food_id):
    food = Food.query.get(food_id)

    db.session().delete(food)
    db.session().commit()

    return redirect(url_for("animals_index"))
