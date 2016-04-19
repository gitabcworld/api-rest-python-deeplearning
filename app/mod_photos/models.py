from app.data import db
from app.data import CRUDMixin

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

class Photo(Base,CRUDMixin):
    __tablename__='photo'
    uuid = db.Column(db.String(128), nullable=False)
    filepath = db.Column(db.String(500), nullable=False)
   

    def __init__(self,uuid,filepath):
	self.uuid = uuid
	self.filepath = filepath

    def get_id(self):
	return self.id

    def serialize(self):
	return {'uuid':self.uuid}
    def serialize_all(self):
	return {'uuid':self.uuid, 'filepath': self.filepath}
    def __repr__(self):
	return '<photo uuid=%r filepath=%r>' % (self.uuid,self.filepath)
        

