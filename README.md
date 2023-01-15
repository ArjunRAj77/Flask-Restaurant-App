# Flask-Restaurant-App
A simple flask application for restaurant.

# Requirements

1. Run the following command in command shell :
    `pip install -r requirements.txt` and make sure that mySQL is installed before the first command.
## Installation procedure

1. Install mySql and mySQL workbench first. Source : [mySql installation on macOS](https://database.guide/install-mysql-on-a-mac/)

2. Open mySQL server using the following command :
    `brew services start mysql` and then run the following command :
    `mysql -uroot`
3. Create a database name `restaurant` and use it.

## POSTMAN API Call Procedure

### 1. Sign Up API  
To make a POST request to the SignUpAPI endpoint using Postman, you would need to configure the following:

- In the URL field, enter the full URL of your endpoint, including the host and port. For example, if your Flask app is running on http://localhost:5000 and the endpoint is /signup, the full URL would be http://localhost:5000/signup.

- In the Headers section, add a key-value pair with the key Content-Type and the value application/json.

- In the Body section, select the raw option, and enter a JSON object containing the required fields for the SignUpRequest schema.

- In Authorization tab, select the type of authorization you want to use, in this case, it is application secret key

- Add the key in the value field of the authorization tab

- Finally, click the Send button to make the POST request.

image.png

### 2. Login API  
To make a POST request to the LoginAPI endpoint using Postman, you would need to configure the following:

- In the URL field, enter the full URL of your endpoint, including the host and port. For example, if your Flask app is running on http://localhost:5000 and the endpoint is /signup, the full URL would be http://localhost:5000/login.

- In the Headers section, add a key-value pair with the key Content-Type and the value application/json.

- In the Body section, select the raw option, and enter a JSON object containing the required fields for the LoginRequest schema.

- In Authorization tab, select the type of authorization you want to use, in this case, it is application secret key

- Add the key in the value field of the authorization tab

- Finally, click the Send button to make the POST request.

image.png

### 3. Logout API
To make a POST request to the LogoutAPI endpoint using Postman, you would need to configure the following:

- In the URL field, enter the full URL of your endpoint, including the host and port. For example, if your Flask app is running on http://localhost:5000 and the endpoint is /signup, the full URL would be http://localhost:5000/logout.

- In the Headers section, add a key-value pair with the key Content-Type and the value application/json.

- In Authorization tab, select the type of authorization you want to use, in this case, it is application secret key

- Add the key in the value field of the authorization tab

- Finally, click the Send button to make the POST request.

### 4. Add Vendor API
- This API should take “user_id” as a parameter.

### 5. Get Vendors API
- Only logged-in users can call this API. 
- This should return all the vendor details with their store and item offerings.

### 6. Add Item API
- This API should be of the following structure
```
{   
    "item_id":"",
    "item_name":"",
    "calories_per_gm":0,
    "available_quantity":0,
    "restaurant_name":"",
    "unit_price":0
}
```

### 7. List Items API
- It list all the items in the inventory

### 8. Create Item Order API
- API for creating an item order 
- input parameters:
```
{   
    "user_id":"",
    "item_id":"",
    "quantity":0

}
```

### 9. Place Order API
- Only logged-in customers can place orders.
- This API should take “order_id” as a parameter.

### 10. List Orders By CustomerAPI
- Only logged-in users can call this API. 
- This returns all the orders placed by that customer.
- This should take “customer_id” as a parameter.

### 11. List All Orders API
- Only the admin can call this API.
- This API returns all the orders in the orders table.