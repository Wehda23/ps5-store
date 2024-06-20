# PlayStation Store Backend

This project is about creating a playstation store which represents a simple E-commerce website using Flask as the backend technology.

## Main Flask Application

In this folder, you will find the Flask application assembled and ready to run. The application is divided into several folders and files for better organization and maintainability. Below is a breakdown of the directory structure and the purpose of each component.

### Directory Structure

```txt
project_root/
    playstation/
        __init__.py
        app.py
        README.md
        routes.py
        database.py
        settings.py
        admin/
            __init__.py
            permissions.py
            authentications/
                __init__.py
                jwt_authentication.py
                token.py
        applications/
            __init__.py
            pages/
                __init__.py
                app.py
            users/
                __init__.py
                app.py
            products/
                __init__.py
                app.py
            orders/
                __init__.py
                app.py
            swagger/
                __init__.py
        models/
            __init__.py
            user.py
            products.py
            orders.py
            coupons.py
            payments.py
            shipping_addresses.py
        serializers/
            __init__.py
            serializer.py
    templates/
        home_page/
            index.html
        login_page/
            index.html
    static/
        css/
        js/
        images/
        swagger_config.json
```

## Create Virtual Enviroment

If you are running this project in a development stage it is adviced to use python virtual inveiroment

- To create virtual enviroment

```bash
python -m venv venv
```

- To Run virtual enviroment

```bash
venv\Scripts\activate
```

## Run Application

To run the application, you need to have Python installed on your machine.

- Make sure to install dependencies from the file `requirements.txts`

```bash
pip install -r requirements.txt
```

- You can run the application by executing the following command in your terminal:

```bash
python app.py
```

## Database Schema

This project utilizes the following database schema to manage and organize data efficiently. The schema defines the structure, relationships, and constraints for the database tables.

![Database Schema](https://i.imghippo.com/files/GQdfW1717777832.png)

The diagram provides a visual representation of the tables, columns, and their relationships, ensuring a clear understanding of the data flow and organization within the system.


# Playstation Packages for backend project

This package contains the packages & Applications required for Play Station Store application.

1. admin
2. applications
3. models
4. serializers

# Admin Package

The admin package contains modules related to the administration of the application, such as managing user permissions and authentication mechanisms.

# Applications Package

The applications package is divided into sub-packages, each responsible for different functional areas of the application, such as:

- pages: Manages the different pages of the application.
- users: Handles user-related operations.
- products: Manages product-related functionalities.
- orders: Deals with order processing and management.
- swagger: Contains configuration for API documentation using Swagger.

## Users Application

### User Registration API

This API handles the registration of new users by validating the provided data and creating a new user account.

### Endpoint

### Register User

- **URL**: `/api/users/register`
- **Method**: `POST`
- **Content-Type**: `application/json`

#### Request Body

The following fields are required in the request body:

- `first_name` (string): The first name of the user.
- `last_name` (string): The last name of the user.
- `email` (string): The email address of the user.
- `password` (string): The password for the user account.

#### Response

- **Success (201)**: Registration is successful.
  - **Body**: `Successful Registration`
- **Error (403)**: Validation error.
  - **Body**: List of validation errors.
- **Error (409)**: Email already registered.
  - **Body**: `Email is already registered`
- **Error (400)**: Registration failed.
  - **Body**: `Registration Failed`

### Example Usage

### Using JavaScript Fetch

```javascript
const url = '/api/users/register';
const data = {
    first_name: 'John',
    last_name: 'Doe',
    email: 'john.doe@example.com',
    password: 'securePassword123'
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
```

### Using JavaScript axios

```js
const axios = require('axios');

const url = '/api/users/register';
const data = {
    first_name: 'Jane',
    last_name: 'Doe',
    email: 'jane.doe@example.com',
    password: 'securePassword123'
};

axios.post(url, data, {
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => {
    console.log('Success:', response.data);
})
.catch(error => {
    console.error('Error:', error.response.data);
});

```

### Error Handling

When the registration fails due to validation errors or an already registered email, the response will contain appropriate status codes and error messages. Ensure to handle these responses in your frontend application.

### Status Codes

-   `201`: Created - Registration was successful.
-   `403`: Forbidden - Validation errors occurred.
-   `409`: Conflict - Email is already registered.
-   `400`: Bad Request - Registration failed due to an unspecified error.

### Notes

-   Make sure your backend server is running and accessible at the base URL specified in the `fetch` or `axios` call.

-   Proper error handling should be implemented to provide feedback to the user in case of registration failure.

## Register Flask Blueprints to Flask

By using the function `routes` in the file `./routes.py` we can register all our flask blueprints to Flask application

Here is an example of how to set it up:

```py
from flask import Flask
from playstation.routes import routes


# Initiate flask application
app: Flask = Flask(__name__)

# Register routes
routes(app)


if __name__ == "__main__":
    # Run flask application
    app.run()
```

## Models Package

The models package defines the database models for the application. Each model represents a table in the database and includes:

- user.py: User model.
- products.py: Product model.
- orders.py: Order model.
- coupons.py: Coupon model.
- payments.py: Payment model.
- shipping_addresses.py: Shipping Address model.

### Initiate Flask Database Configuration and Models

By using the function `database` in the file `./database.py` we can initiate flask database configurations and models

Here is an example of how to set it up:

```py
from flask import Flask
from playstation.database import database


# Initiate flask application
app: Flask = Flask(__name__)

# Register routes
database(app)


if __name__ == "__main__":
    # Run flask application
    app.run()
```

## Serializers Package

Explain the package