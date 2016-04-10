from app.data import db
from app.data import CRUDMixin

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

class Winner(Base, CRUDMixin):
    #User name
    __tablename__= 'winner'
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Winner %r>' % (self.name)

