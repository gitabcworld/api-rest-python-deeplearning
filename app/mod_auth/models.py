from app.data import db
from app.data import CRUDMixin

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified =db.Column(db.DateTime, default=db.func.current_timestamp(),
                                        onupdate=db.func.current_timestamp())

class User(Base, CRUDMixin):
    __tablename__= 'auth_user'
    #User name
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False,
                                    unique=True)
    
    password = db.Column(db.String(192), nullable=False)

    #Authorisation Data: role & status
    #role = db.Column(db.SmallInteger, nullable=False)
    #status = db.Column(db.SmallInteger, nullable=False)

    #New instance instanttion procedure

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def is_authenticated(self):
	return True
    def is_active(self):
	return True
    def is_anonymous(self):
	return True
    def get_id(self):
	return self.id

    def __repr__(self):
        return '<User %r>' % (self.name)
        

