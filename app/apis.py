from app import application
from flask import jsonify, Response, session
from app.models import *
from app import *
import uuid
import datetime
from marshmallow import Schema, fields
from flask_restful import Resource, Api
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import json


class SignUpRequest(Schema):
    name = fields.Str(default = "name")
    username = fields.Str(default = "username")
    password = fields.Str(default = "password")
    level = fields.Integer(default=0)

class APIResponse(Schema):
    message = fields.Str(default="Success")

# class ItemSchema(Schema):
#     item_id = fields.String()
#     item_name = fields.String()
#     calories_per_gm = fields.Integer()
#     available_quantity = fields.Integer()
#     restaurant_name = fields.String()
#     unit_price = fields.Integer()
class VendorSchema(Schema):
    vendor_id = fields.String()
    store_name = fields.String()
    item_offerings = fields.String()


class VendorAPIResponse(Schema):
    message = fields.Str(default="Success")
    vendors = fields.List(fields.Nested(VendorSchema))

class LoginRequest(Schema):
    username = fields.Str(default="username")
    password = fields.Str(default="password")
    
#  Restful way of creating APIs through Flask Restful
class AddItemRequest(Schema):
    item_id=fields.Str(default="1")
    item_name=fields.Str(default="name")
    calories_per_gm=fields.Integer(default=0)
    available_quantity=fields.Integer(default=0)
    restaurant_name=fields.Str(default="restaurant_Name")
    unit_price=fields.Integer(default=0)
class AddVendorRequest(Schema):
    user_id=fields.Str(default="user id")
# This is a signup API. This should take, “name,username, password,level” as parameters.
#  Here, the level is 0 for the customer, 1 for the vendor and 2 for Admin.
class SignUpAPI(MethodResource, Resource):
    @doc(description='Sign Up API', tags=['SignUp API'])
    @use_kwargs(SignUpRequest, location=('json'))
    @marshal_with(APIResponse)  # marshalling
    def post(self, **kwargs):
        try:
            user = User(
                uuid.uuid4(), 
                kwargs['name'], 
                kwargs['username'], 
                kwargs['password'], 
                kwargs['level'])
            db.session.add(user)
            db.session.commit()
            return APIResponse().dump(dict(message='User is successfully registerd')), 200
            # return jsonify({'message':'User is successfully registerd'}), 200
        
        except Exception as e:
            print(str(e))
            return APIResponse().dump(dict(message=f'Not able to register user : {str(e)}')), 404
            # return jsonify({'message':f'Not able to register user : {str(e)}'}), 400
    pass 

api.add_resource(SignUpAPI, '/signup')
docs.register(SignUpAPI)

# This API should take the username and passwordof signed-up users andsuccessfully log them in. 
class LoginAPI(MethodResource, Resource):
    @doc(description='Login API', tags=['Login API'])
    @use_kwargs(LoginRequest, location=('json'))
    @marshal_with(APIResponse)  # marshalling
    def post(self, **kwargs):
        try:
            user = User.query.filter_by(username=kwargs['username'], password = kwargs['password']).first()
            if user:
                print('logged in')
                session['user_id'] = user.user_id
                print(f'User id : {str(session["user_id"])}')
                return APIResponse().dump(dict(message='User is successfully logged in')), 200
                # return jsonify({'message':'User is successfully logged in'}), 200
            else:
                return APIResponse().dump(dict(message='User not found')), 404
                # return jsonify({'message':'User not found'}), 404
        except Exception as e:
            print(str(e))
            return APIResponse().dump(dict(message=f'Not able to login user : {str(e)}')), 400
            # return jsonify({'message':f'Not able to login user : {str(e)}'}), 400
    pass
         
api.add_resource(LoginAPI, '/login')
docs.register(LoginAPI)

# This API should log out the customer.
class LogoutAPI(MethodResource, Resource):
    @doc(description='Logout API', tags=['Logout API'])
    @marshal_with(APIResponse)  # marshalling
    def post(self, **kwargs):
        try:
            if session['user_id']:
                session['user_id'] = None
                print('logged out')
                return APIResponse().dump(dict(message='User is successfully logged out')), 200
                # return jsonify({'message':'User is successfully logged out'}), 200
            else:
                print('user not found')
                return APIResponse().dump(dict(message='User is not logged in')), 401
                # return jsonify({'message':'User is not logged in'}), 401
        except Exception as e:
            print(str(e))
            return APIResponse().dump(dict(message=f'Not able to logout user : {str(e)}')), 400
            # return jsonify({'message':f'Not able to logout user : {str(e)}'}), 400    pass
            

api.add_resource(LogoutAPI, '/logout')  
docs.register(LogoutAPI)

# Only added customers can be made vendors.This API should take“user_id” as a parameter.
class AddVendorAPI(MethodResource, Resource):
    @doc(description="Add a vendor",tags=['add_vendor API'])
    @use_kwargs(AddVendorRequest,location=('json'))
    @marshal_with(APIResponse) # marshalling
    def post(self,**kwargs):
        try:
            if session['user_id']:
                user_id = kwargs['user_id']
                user_type=User.query.filter_by(user_id=user_id).first().level
                print(user_id)
                if(user_type ==0):
                    User.level = 1
                    db.session.commit()
                    return APIResponse().dump(dict(message="Customer is upgraded to vendor")),200
                else :
                    return APIResponse().dump(dict(message="Customer is already a vendor")),405
            else:
                return APIResponse().dump(dict(message="Customer is not logged in")),401
        except Exception as e :
            print(str(e))
            return  APIResponse().dump(dict(message=f"Not able to upgrade to vendor:  {e}")),400
    pass
            

api.add_resource(AddVendorAPI, '/add_vendor')
docs.register(AddVendorAPI)

# Only logged-in users can call thisAPI. This should return all the vendor details with their store and item offerings.
class GetVendorsAPI(MethodResource, Resource):
    @doc(description="Get vendors API", tags=['Vendors API'])
    @marshal_with(APIResponse)
    def get(self):
        try:
            if session['user_id']:
                vendors = Item.query.all()
                vendor_list = []
                for vendor in vendors:
                    vendor_data = {
                        'vendor_id': vendor.vendor_id,
                        'store_name': vendor.restaurant_name,
                        'item_offerings': Item.query.filter_by(vendor_id=vendor.vendor_id).all()
                    }
                    vendor_list.append(vendor_data)
                return VendorAPIResponse().dump(dict(vendors=vendor_list)), 200
            else:
                return VendorAPIResponse().dump(dict(message="User is not logged in")), 401
        except Exception as e:
            print(str(e))
            return VendorAPIResponse().dump(dict(message=f"Not able to list vendors: {str(e)}")), 400
    pass
            

api.add_resource(GetVendorsAPI, '/list_vendors')
docs.register(GetVendorsAPI)

# Only logged-in vendors can add items. 
# This API should take, “item_id,item_name, restaurant_name, available_quantity, unit_price, calories_per_gm”.
class AddItemAPI(MethodResource, Resource):
    @doc(description="Add an item API",tags=['item API'])
    @use_kwargs(AddItemRequest,location=('json'))
    @marshal_with(APIResponse) # marshalling
    def post(self,**kwargs):
        try:
            if session['user_id']:
                user_id = session['user_id']
                user_type=User.query.filter_by(user_id=user_id).first().level
                print(user_id)
                if(user_type ==1):
                    item=Item(
                        kwargs['item_id'],
                        user_id,
                        kwargs['item_name'],
                        kwargs['calories_per_gm'],
                        kwargs['available_quantity'],
                        kwargs['restaurant_name'],
                        kwargs['unit_price']
                    )
                    db.session.add(item)
                    db.session.commit()
                    return APIResponse().dump(dict(message="Item is succesfully created")),200
                else :
                    return APIResponse().dump(dict(message="Logged in User is not a vendor")),405
            else:
                return APIResponse().dump(dict(message="Vendor is not logged in")),401
        except Exception as e :
            print(str(e))
            return  APIResponse().dump(dict(message=f"Not able to list vendors:  {e}")),400

    pass
            

api.add_resource(AddItemAPI, '/add_item')
docs.register(AddItemAPI)


class ListItemsAPI(MethodResource, Resource):
    pass

api.add_resource(ListItemsAPI, '/list_items')
docs.register(ListItemsAPI)


class CreateItemOrderAPI(MethodResource, Resource):
    pass
            

api.add_resource(CreateItemOrderAPI, '/create_items_order')
docs.register(CreateItemOrderAPI)

# Only logged-in customers can place orders.This API should take“order_id” as a parameter.
class PlaceOrderAPI(MethodResource, Resource):
    pass
            

api.add_resource(PlaceOrderAPI, '/place_order')
docs.register(PlaceOrderAPI)

# Only logged-in users cancall this API. Thisreturns all the orders placed by that customer.
#  This should take “customer_id” asa parameter.
class ListOrdersByCustomerAPI(MethodResource, Resource):
    pass
            

api.add_resource(ListOrdersByCustomerAPI, '/list_orders')
docs.register(ListOrdersByCustomerAPI)

# Only the admin can call this API.This API returns all the ordersin the orders table.
class ListAllOrdersAPI(MethodResource, Resource):
    pass
            
api.add_resource(ListAllOrdersAPI, '/list_all_orders')
docs.register(ListAllOrdersAPI)