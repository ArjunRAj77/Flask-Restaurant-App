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