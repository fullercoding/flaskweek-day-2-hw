from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL
from app import db, login
from flask_login import UserMixin #####  THIS IS ONLY FOR THE USER MODEL
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    icon = db.Column(db.Integer)
    
    #should return a unique identifying string (for computer to read)
    def __repr__(self):
        return f'<User: {self.email} | {self.id} >'
    
    # Human Readable
    def __str__(self):
        return f'<User: {self.email} | {self.first_name} {self.last_name} >'
    
    #salt and hash our password to make it harder to steal
    def hash_password(self, original_password):
        return generate_password_hash(original_password)
    
    #Check the hashed password(self.password) to the password they are using at login
    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)


    def save(self):
        db.session.add(self) #add the user to our session
        db.session.commit() #saves the session
    
    def from_dict(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])