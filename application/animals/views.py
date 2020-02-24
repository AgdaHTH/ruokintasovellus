from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.animals.models import Animal
from application.animals.models import Food
from application.auth.models import User
from application.animals.forms import AnimalForm, UserForm, FoodForm

@app.route("/animals/current/", methods=["GET"])
@login_required
def current_animals():
        
    owner = current_user
    omistajaid = owner.get_id()   
    
    return render_template("animals/current.html", form = FoodForm(), 
        currentanimals = User.find_animals_of_current_user(omistajaid), currentfoods = User.find_foods_of_current_user(omistajaid),
        counts = User.count_animals_of_current_user(omistajaid))

@app.route("/animals/", methods=["GET"])
def animals_index():    
    return render_template("animals/list.html", animals = Animal.query.all(), foods = Food.query.all())

#@app.route("/animals/<food_id>/", methods=["GET"])
#def foods_animals(food_id):    
#    return render_template("animals/foods.html", animals = Food.list_foods_and_animals(food_id))

@app.route("/animals/<animal_id>/", methods=["GET"])
def animals_show_animal(animal_id):
    
    animal = Animal.query.get(animal_id)
    
    return render_template("animals/show.html", owner = User.query.get(animal.account_id), 
        animal = Animal.query.get(animal_id), foods = Food.find_foods(animal_id), allfoods = Food.query.all())

@app.route("/animals/delete/<animal_id>", methods=["GET"])
@login_required
def animals_delete(animal_id):
    
    animal = Animal.query.get(animal_id)
    
    db.session().delete(animal)
    db.session().commit()

    return redirect(url_for("current_animals"))

@app.route("/animals/food/delete/<food_id>")
def foods_delete(food_id):
    food = Food.query.get(food_id)

    db.session().delete(food)
    db.session().commit()

    return redirect(url_for("animals_index"))


@app.route("/animals/new/")
@login_required
def animals_form():
    return render_template("animals/new.html", form = AnimalForm())

@app.route("/animals/newuser/")
def animals_userform():
    return render_template("animals/newuser.html", form = UserForm())

@app.route("/animals/", methods=["POST"])
@login_required
def animals_create():
    form = AnimalForm(request.form)

    if not form.validate():
        return render_template("animals/new.html", form = form)

    animal = Animal(form.name.data)
    animal.account_id = current_user.id 

    db.session().add(animal)
    db.session().commit()
  
    return redirect(url_for("animals_index"))

@app.route("/animals/newuser/", methods=["POST"])
def users_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("animals/newuser.html", form = form)

    user = User(form.name.data, form.username.data, form.password.data)
        
    db.session().add(user)
    db.session().commit()

    return redirect(url_for("animals_index"))

@app.route("/animals/newfood/", methods=["POST"])
def add_food():
    form = FoodForm(request.form)

    if not form.validate():
        return render_template("animals/current.html", form = form)
   
    food = Food(form.name.data)

    db.session().add(food)
    db.session().commit()

    return redirect(url_for("animals_index"))

@app.route("/animals/newfood/", methods=["GET"])
def new_food_form():
    return render_template("animals/newfood.html", form = FoodForm())


@app.route("/animals/newfood/add/<animal_id>/<food_id>", methods=["POST"]) 
def food_add(animal_id, food_id):
    
    #animal = db.session.query(Animal).get(animal_id)
    #food = db.session.query(Food).get(food_id)
    animal = Animal.query.get(animal_id)
    food = Food.query.get(food_id)
    

    print("eläinnumero:")
    print(animal_id)
    print("ruokanumero:")
    print(food_id)

    db.session().add(food)
    db.session().add(animal)

    animal.foods.append(food)  
    db.session().commit()

    return redirect(url_for("animals_show_animal", animal_id=animal.id))

@app.route("/animals/foods/<food_id>")
def show_animals_per_food(food_id):
    return render_template("animals/foods.html", animals = Food.list_foods_and_animals(food_id))

@app.route("/animals/<animal_id>/", methods=["POST"])
def animals_set_sick(animal_id):

    animal = Animal.query.get(animal_id)
    if animal.sick == False:
	    animal.sick = True
    else:
        animal.sick = False
    
    db.session().commit()
  
    return redirect(url_for("current_animals"))