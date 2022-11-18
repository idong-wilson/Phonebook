from app import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(20), unique=True, nullable=False)
    last_name=db.Column(db.String(20), unique=True, nullable=False)
    phone_number=db.Column(db.String(20), unique=True, nullable=False)
    address=db.Column(db.String(20), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self):
        return f'{self.first_name} : {self.last_name} : {self.phone_number} : {self.address} : {self.date_created}'
    