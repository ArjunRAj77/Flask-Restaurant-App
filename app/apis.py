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

#  Restful way of creating APIs through Flask Restful

# This is a signup API. This should take, “name,username, password,level” as parameters.
#  Here, the level is 0 for the customer, 1 for the vendor and 2 for Admin.
class SignUpAPI(MethodResource, Resource):
    pass 

api.add_resource(SignUpAPI, '/signup')
docs.register(SignUpAPI)

# This API should take the username and passwordof signed-up users andsuccessfully log them in. 
class LoginAPI(MethodResource, Resource):
    pass
            

api.add_resource(LoginAPI, '/login')
docs.register(LoginAPI)

# This API should log out the customer.
class LogoutAPI(MethodResource, Resource):
    pass
            

api.add_resource(LogoutAPI, '/logout')
docs.register(LogoutAPI)

# Only added customers can be made vendors.This API should take“user_id” as a parameter.
class AddVendorAPI(MethodResource, Resource):
    pass
            

api.add_resource(AddVendorAPI, '/add_vendor')
docs.register(AddVendorAPI)

# Only logged-in users can call thisAPI. This should return allthe vendor details with their store and item offerings.
class GetVendorsAPI(MethodResource, Resource):
    pass
            

api.add_resource(GetVendorsAPI, '/list_vendors')
docs.register(GetVendorsAPI)

# Only logged-in vendors can add items. 
# This API should take, “item_id,item_name, restaurant_name, available_quantity, unit_price, calories_per_gm”.
class AddItemAPI(MethodResource, Resource):
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