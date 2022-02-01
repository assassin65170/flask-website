from website import db, login_manager
from flask_login import UserMixin
from website import bcrypt

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Contact(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    subject = db.Column(db.String(length=50), nullable=False)
    message = db.Column(db.String(length=300), nullable=False)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=50),nullable=False)


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)



    def __repr__(self):
        return f'Contact:{self.email_address} {self.username} {self.subject} {self.message}'








