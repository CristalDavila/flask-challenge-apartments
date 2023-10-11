from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import API, Resource
from models import Apartment, Tenant, Lease


from models import db, Tenant

#import ipdb

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

migrate = Migrate( app, db )
db.init_app( app )


if __name__ == '__main__':
    app.run( port = 3000, debug = True )


@app.route('/apartments/<int:id>', methods=['GET','POST', 'DELETE'])
def apartment_by_id(id):
    apartment = Apartment.query.filter(Apartment.id == id).first()

    if apartment.method == 'GET':
        apartment_dict = apartment.to_dict()

        response = make_response(
            apartment_dict,
            200
        )

        return response

    elif apartment.method == 'DELETE':
        db.session.delete(apartment)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "apartment deleted."    
        }

        response = make_response(
            response_body,
            200
        )
    
    elif apartment.method == 'POST':
        db.session.post(apartment)
        db.session.commit()

        response_body = {
            "post_successful": True,
            "message": "apartment posted"
        }

        response = make_response(
            response_body,
            200

        )

@app.route('/tenant/<int:id>', methods= ['GET', 'POST', 'DELETE'])
def tentant_by_id(id):
    tenant = Tenant.query.filter(Tenant.id == id).first()

    if tenant.method == 'GET':
        tenant_dict = tenant.to_dict()

        response = make_response(
            tenant_dict,
            200
        )

        return response

    elif tenant.method == 'DELETE':
        db.session.delete(tenant)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "tenant deleted."    
        }

        response = make_response(
            response_body,
            200
        )
    
    elif tenant.method == 'POST':
        db.session.post(tenant)
        db.session.commit()

        response_body = {
            "post_successful": True,
            "message": "tenant posted"
        }

        response = make_response(
            response_body,
            200

        )
           
@app.route('/lease/<int:id>', methods= ['POST', 'DELETE'])
def lease_by_id(id):
    lease = Lease.query.filter(Lease.id == id).first()

    if lease.method == 'DELETE':
        db.session.delete(lease)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "lease deleted"    
        }

        response = make_response(
            response_body,
            200
        )
        return response

    
    elif lease.method == 'POST':
        db.session.post(lease)
        db.session.commit()

        response_body = {
            "post_successful": True,
            "message": "lease posted"
        }

        response = make_response(
            response_body,
            200

        )
           
