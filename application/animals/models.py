from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy import Table, Column, Integer, ForeignKey

animals_foods = db.Table('animalsfoods', Base.metadata,
    db.Column('animal_id', db.Integer, db.ForeignKey('animal.id')),
    db.Column('food_id', db.Integer, db.ForeignKey('food.id')))

class Animal(Base):      
    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    user = db.relationship("User", backref='animal', lazy=True) 
    foods = db.relationship("Food", secondary=animals_foods, back_populates='animals', lazy='dynamic')
    sick = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name 
        self.sick = False      
    
class Food(Base):
    name = db.Column(db.String(144), unique=True, nullable = False) #unique lisätty
    animals = db.relationship("Animal", secondary=animals_foods, back_populates='foods', lazy='dynamic')
    price = db.Column(db.Integer, nullable = True)
    
    def __init__(self, name):
        self.name = name

    @staticmethod
    def set_price(food_id, newprice):
        price = text("UPDATE Food"
        " SET price = :newprice"
        " WHERE id = :food_id").params(food_id=food_id, newprice=newprice)

        db.engine.execute(price)

    @staticmethod
    def find_foods(animal_id):
        stmt = text("SELECT Food.name FROM Food"
        " LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id"
        " LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id"
        " WHERE Animal.id = :animal_id"
        " GROUP BY Food.name").params(animal_id=animal_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name":row[0]})
        return response
    
    @staticmethod
    def list_foods_and_animals(food_id):
        query2 = text("SELECT Animal.name FROM Food"
        " LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id"
        " LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id"
        " WHERE Food.id = :food_id").params(food_id=food_id)

        res = db.engine.execute(query2)

        response = []

        for row in res:
            response.append({"name":row[0]})
        return response