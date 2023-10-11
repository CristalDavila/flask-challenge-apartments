from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class Tenant(db.model):
    __tablename__ = 'tenant'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    
apartments = db.relationship(
    'Apartment',back_populates='tenants')

def __repr__(self):
    return f'<Tenant {self.id}, {self.name}, {self.age}>'

class Lease(db.model):
    __tablename__ = 'lease'

    id = db.Column(db.Integer, primary_key= True)
    rent = db.Column(db.Float)

    #foreign keys for tenant and apartment
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'))
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'))
    
    #establish relationships between databases
    tenant = db.relationship('tenant', back_populates='lease')
    apartment = db.relationship('apartment', back_populates='lease')
    

class Apartment(db.model):
    __tablename__ = 'apartment'

    id = db.Column(db.Integer, primary_key= True)
    number = db.Column(db.Integer)

tenants = db.relationship(
    'Tenant', back_populates='apartments')
   
def __repr__(self):
    return f'<Apartment {self.id}, {self.number}>'

