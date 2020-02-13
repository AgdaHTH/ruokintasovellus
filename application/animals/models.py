from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy import Table, Column, Integer, ForeignKey

association_table = db.Table('association', Base.metadata,
    db.Column('animal_id', db.Integer, db.ForeignKey('animal.id')),
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'))
)

class Animal(Base):      
    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    user = db.relationship("User", backref='animal', lazy=True) 
    food = db.relationship("Food", secondary=association_table, back_populates='animal', lazy=True) #pitääkö olla lazy =True

    def __init__(self, name):
        self.name = name       
    
class Food(Base):
    name = db.Column(db.String(144), nullable = False)
    #täällä voisi sitten olla hinta-sarake
    #animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable = False)
    animal = db.relationship("Animal", secondary=association_table, back_populates='food', lazy=True)
    

    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def find_foods(animal_id):
        stmt = text("SELECT Food.name FROM Food"
        " LEFT JOIN association ON association.food_id = Food.id"
        " LEFT JOIN Animal ON Animal.id = association.animal_id"
        " WHERE Animal.id = :animal_id"
        " GROUP BY Food.name").params(animal_id=animal_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name":row[0]})
        return response
    
        

