from application import db
from application.models import Base
from sqlalchemy.sql import text

#association_table = Table('association', Base.metadata,
#    Column('left_id', Integer, ForeignKey('left.id')),
#    Column('right_id', Integer, ForeignKey('right.id'))
#)

class Animal(Base):      
    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    user = db.relationship("User", backref='animal', lazy=True) 

    def __init__(self, name):
        self.name = name       
    
class Food(Base):
    name = db.Column(db.String(144), nullable = False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable = False)
    animal = db.relationship("Animal", backref='food', lazy=True)

    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def find_foods(animal_id):
        stmt = text("SELECT Food.name FROM Food"
        " WHERE Food.animal_id = :animal_id"
        " GROUP BY Food.name").params(animal_id=animal_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name":row[0]})
        return response
    
        

