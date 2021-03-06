from application import db
from application.models import Base
from sqlalchemy.sql import text
class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    animals = db.relationship("Animal", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    @staticmethod
    def find_animals_of_current_user(account_id):
        
        stmt = text("SELECT * FROM Animal" 
        " JOIN Account ON Account.id = Animal.account_id"
        " WHERE account_id = :account_id").params(account_id=account_id)
        
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"id":row[0], "time1":row[1], "time2":row[2], "name":row[3], "sick":row[5]})
        return response
    
    @staticmethod
    def count_animals_of_current_user(account_id):

        query1 = text("SELECT COUNT(Account.id) FROM Animal"
        " LEFT JOIN Account ON Account.id = Animal.account_id"
        " WHERE Animal.account_id = :account_id").params(account_id=account_id)

        res = db.engine.execute(query1)
        response = []
        for row in res:
            response.append({"count":row[0]})
        return response
    
    @staticmethod
    def average_of_food_prices(account_id):
        query2 = text("SELECT AVG(Food.price) FROM Food"
        " LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id"
        " LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id" 
        " LEFT JOIN Account ON Account.id = Animal.account_id"
        " WHERE Account.id = :account_id").params(account_id=account_id)
    
        res = db.engine.execute(query2)
        response = []

        for row in res:
            response.append({"average":row[0]})
        return response

    @staticmethod
    def find_foods_of_current_user(account_id):
        stmt = text("SELECT Food.name FROM Food"
        " LEFT JOIN animalsfoods ON animalsfoods.food_id = Food.id"
        " LEFT JOIN Animal ON Animal.id = animalsfoods.animal_id" 
        " LEFT JOIN Account ON Account.id = Animal.account_id"
        " WHERE Account.id = :account_id"
        " GROUP BY Food.name").params(account_id=account_id)
        
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"name":row[0]})
        return response