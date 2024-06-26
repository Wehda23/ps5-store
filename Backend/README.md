# PlayStation Store Backend

This project is about creating a playstation store which represents a simple E-commerce website using Flask as the backend technology.
## Table of Contents
1. [Introduction](#introduction)
2. [Main Flask Application](#main-flask-application)
3. [Create Virtual Environment](#create-virtual-environment)
4. [Run Application](#run-application)
5. [Database Schema](#database-schema)
6. [Swagger Application](#swagger-application)
7. [Users Application](#users-application)
8. [Register Flask Blueprints to Flask](#register-flask-blueprints-to-flask)
9. [File Handler Package](#file-handler-package)
10. [Initializing Loggers in Flask](#initializing-loggers-in-flask)
11. [Support my work](#support-my-Work)

## Introduction

The project includes the following features:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

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
        logger.py
        settings.py
        admin/
            __init__.py
            permissions.py
            authentications/
                __init__.py
                jwt_authentication.py
                token.py
            file_manager/
                __init__.py
                file_handler.py
                image_handler.py
                storage.py
                exceptions.py
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
            shipping_addresses/
                __init__.py
                app.py
            payments/
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
            blacklisted_tokens.py
            exceptions.py
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
5. file_manager

# Admin Package

The admin package contains modules related to the administration of the application, such as managing user permissions and authentication mechanisms.

# Applications Package

The applications package is divided into sub-packages, each responsible for different functional areas of the application, such as:

- pages: Manages the different pages of the application.
- users: Handles user-related operations.
- products: Manages product-related functionalities.
- orders: Deals with order processing and management.
- swagger: Contains configuration for API documentation using Swagger.
- payments: Handles payment related Operations.
- shipping_addresses: Handles shipping addresses operations.

## Swagger Application

The Swagger Application provides interactive API documentation for the PlayStation Store Backend. It allows developers to explore and test the available API endpoints directly from the browser.

### Swagger Configuration

The Swagger UI is configured using the `flask_swagger_ui` package. Below is a summary of the configuration:

- **URL**: `/docs`
- **Swagger Config File**: `static/swagger_config.json`
- **Application Name**: "Play Station 5 Store"

![Swagger](https://i.postimg.cc/CL4jvR4s/Screenshot-58.png)

## Users Application

### User Registration API

This API handles the registration of new users by validating the provided data and creating a new user account.

<hr/>

### Register User Endpoint

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

<hr/>

### Login User Endpoint

- **URL**: `/api/users/login`
- **Method**: `POST`
- **Content-Type**: `application/json`

#### Request Body

The following fields are required in the request body:

- `email` (string): The email address of the user.
- `password` (string): The password for the user account.

#### Response

- **Success (201)**: Login is successful.
  - **Body**:
    ```json
    {
      "id": 1,
      "email": "example@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "token": {
        "access": "access token",
        "refresh": "refresh token"
      }
    }
    ```
- **Error (404)**: Validation error or login failed.
  - **Body**: List of validation errors or `Login Failed`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/users/login';
const data = {
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

#### Using JavaScript Axios

```javascript
const axios = require('axios');

const url = '/api/users/login';
const data = {
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

When the login fails due to validation errors or incorrect credentials, the response will contain appropriate status codes and error messages. Ensure to handle these responses in your frontend application.

### Status Codes

-   `201`: Created - Login was successful.
-   `404`: Not Found - Validation errors occurred or login failed.

### Notes

-   Make sure your backend server is running and accessible at the base URL specified in the `fetch` or `axios` call.

-   Proper error handling should be implemented to provide feedback to the user in case of registration failure.

Sure, here is the markdown documentation for the `update_user` endpoint:

<hr/>

### Update User Endpoint

- **URL**: `/api/users/update/<int:pk>`
- **Method**: `PUT`
- **Content-Type**: `application/json`
- **Authentication**: `Bearer Access_token` required

#### Description

Allows authenticated users to update their profile information. The user must be the account owner.

#### Request Body

The following fields can be included in the request body:

- `first_name` (string): The new first name of the user.
- `last_name` (string): The new last name of the user.
- `email` (string): The new email address of the user.

#### Response

- **Success (200)**: Update is successful.
  - **Body**:
    ```json
    {
      "id": 1,
      "first_name": "NewFirstName",
      "last_name": "NewLastName",
      "email": "newemail@example.com"
    }
    ```
- **Error (404)**: Validation error or update failed.
  - **Body**: Error message indicating the cause of failure.

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/users/update/1';
const data = {
    first_name: 'NewFirstName',
    last_name: 'NewLastName',
    email: 'newemail@example.com'
};

fetch(url, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer Access_token'
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

#### Using JavaScript Axios

```javascript
const axios = require('axios');

const url = '/api/users/update/1';
const data = {
    first_name: 'NewFirstName',
    last_name: 'NewLastName',
    email: 'newemail@example.com'
};

axios.put(url, data, {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer Access_token'
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

When the update fails due to validation errors or other issues, the response will contain appropriate status codes and error messages. Ensure to handle these responses in your frontend application.

### Status Codes

-   `200`: OK - Update was successful.
-   `404`: Not Found - Validation errors occurred or update failed.

### Notes

-   Ensure your backend server is running and accessible at the base URL specified in the `fetch` or `axios` call.
-   Proper error handling should be implemented to provide feedback to the user in case of update failure.

<hr/>

### Refresh Token Endpoint

- **URL**: `/api/users/refresh`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Authentication**: `Bearer Refresh_token` required

#### Description

Generates new access and refresh tokens for authenticated users by blacklisting the current tokens.

#### Request Body

The following fields are required in the request body:

- `access` (string): The current access token.
- `refresh` (string): The current refresh token.

#### Response

- **Success (201)**: Tokens refreshed successfully.
  - **Body**:
    ```json
    {
      "access": "new_access_token",
      "refresh": "new_refresh_token"
    }
    ```
- **Error (404)**: Validation error or token refresh failed.
  - **Body**: List of validation errors or `Failed to refresh token`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/users/refresh';
const data = {
    access: 'current_access_token',
    refresh: 'current_refresh_token'
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer refresh_token'
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

#### Using JavaScript Axios

```javascript
const axios = require('axios');

const url = '/api/users/refresh';
const data = {
    access: 'current_access_token',
    refresh: 'current_refresh_token'
};

axios.post(url, data, {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer refresh_token'
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

When the token refresh fails due to validation errors or other issues, the response will contain appropriate status codes and error messages. Ensure to handle these responses in your frontend application.

### Status Codes

-   `201`: Created - Tokens refreshed successfully.
-   `404`: Not Found - Validation errors occurred or token refresh failed.

### Notes

-   Ensure your backend server is running and accessible at the base URL specified in the `fetch` or `axios` call.
-   Proper error handling should be implemented to provide feedback to the user in case of token refresh failure.

<hr/>

### Logout Endpoint

- **URL**: `/api/users/logout`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Authentication**: `Bearer Access_token` required

#### Description

Logs out the authenticated user by blacklisting the current access and refresh tokens.

#### Request Body

The following fields are required in the request body:

- `access` (string): The current access token.
- `refresh` (string): The current refresh token.

#### Response

- **Success (200)**: Logout successful.
  - **Body**:
    ```json
    "Logged out successfully"
    ```
- **Error (404)**: Validation error or logout failed.
  - **Body**: List of validation errors or `Failed to logout`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/users/logout';
const data = {
    access: 'current_access_token',
    refresh: 'current_refresh_token'
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer access_token'
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

#### Using JavaScript Axios

```javascript
const axios = require('axios');

const url = '/api/users/logout';
const data = {
    access: 'current_access_token',
    refresh: 'current_refresh_token'
};

axios.post(url, data, {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer access_token'
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

When the logout fails due to validation errors or other issues, the response will contain appropriate status codes and error messages. Ensure to handle these responses in your frontend application.

### Status Codes

-   `200`: OK - Logout was successful.
-   `404`: Not Found - Validation errors occurred or logout failed.

### Notes

-   Ensure your backend server is running and accessible at the base URL specified in the `fetch` or `axios` call.
-   Proper error handling should be implemented to provide feedback to the user in case of logout failure.

<hr/>

## Products Application

This application manages all product-related actions, including category creation, product creation, updates, and deletion. It defines API routes to facilitate these actions, ensuring secure and efficient product management.

### Get All Product Categories Endpoint

- **URL**: `/api/products/categories`
- **Method**: `GET`
- **Content-Type**: `application/json`

#### Response

- **Success (200)**: Categories retrieved successfully.
  - **Body**: A list of all product categories.
- **Error (404)**: No categories found.
  - **Body**: `Failed to grab product categories`

### Example Usage

### Using JavaScript Fetch

```javascript
const url = '/api/products/categories';

fetch(url, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
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

const url = '/api/products/categories';

axios.get(url, {
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

When the request to retrieve product categories fails, the response will contain appropriate status codes and error messages. Ensure to handle these responses in your frontend application.

### Status Codes

-   `200`: OK - Categories retrieved successfully.
-   `404`: Not Found - No categories found.

### Notes

-   Make sure your backend server is running and accessible at the base URL specified in the `fetch` or `axios` call.

-   Proper error handling should be implemented to provide feedback to the user in case of retrieval failure.

<hr/>

## Create Product Category Endpoint

- **URL**: `/api/category`
- **Method**: `POST`
- **Authentication**: JWT Token (Bearer Token)
- **Permissions**: Admin (IsAdmin)

### Request Body

The request body must include the following JSON object:

```json
{
    "name": "Newcategoryname"
}
```

### Responses

- **Success (200)**: Category created successfully.
  - **Body**: `"Category created successfully"`

- **Error (400)**: Bad Request - Invalid input data.
  - **Body**: List of validation errors.

- **Error (401)**: Unauthorized - User is not authenticated.
  - **Body**: `"Unauthorized"`

- **Error (403)**: Forbidden - User does not have sufficient permissions.
  - **Body**: `"Forbidden"`

### Example Usage

### Using JavaScript Fetch

```javascript
const url = '/api/category';
const data = {
    name: 'Newcategoryname'
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
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

const url = '/api/category';
const data = {
    name: 'Newcategoryname'
};

axios.post(url, data, {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
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

Ensure proper error handling to manage responses for different scenarios like validation errors, authentication failures, and permission denials.

### Status Codes

-   `200`: OK - Category created successfully.
-   `400`: Bad Request - Invalid input data format.
-   `401`: Unauthorized - Authentication credentials missing or invalid.
-   `403`: Forbidden - Insufficient permissions to perform the operation.

### Notes

-   Replace `YOUR_JWT_TOKEN_HERE` with a valid JWT token obtained after successful authentication.
-   The endpoint requires admin permissions (`IsAdmin`) for successful category creation.
-   Implement appropriate frontend and backend validations to handle edge cases and ensure robustness of the API.

<hr/>

### Update Product Category Endpoint

- **URL**: `/api/category/{category_id}`
- **Method**: `PUT`
- **Authentication**: JWT Token (Bearer Token)
- **Permissions**: Admin (IsAdmin)

#### Request Body

The request body can include the following JSON object:

```json
{
    "name": "New_category_name",
    "id": 1
}
```

The `id` field is optional. If not provided, the `category_id` from the URL will be used.

#### Responses

- **Success (200)**: Category updated successfully.
  - **Body**: JSON object representing the updated category.

- **Error (400)**: Bad Request - Invalid input data.
  - **Body**: List of validation errors.

- **Error (401)**: Unauthorized - User is not authenticated.
  - **Body**: `"Unauthorized"`

- **Error (403)**: Forbidden - User does not have sufficient permissions.
  - **Body**: `"Forbidden"`

- **Error (404)**: Not Found - Category not found.
  - **Body**: `"Category not found"`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/category/1';
const data = {
    name: 'UpdatedCategoryName'
};

fetch(url, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
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

#### Using JavaScript axios

```js
const axios = require('axios');

const url = '/api/category/1';
const data = {
    name: 'UpdatedCategoryName'
};

axios.put(url, data, {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
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

Ensure proper error handling to manage responses for different scenarios like validation errors, authentication failures, and permission denials.

### Status Codes

-   `200`: OK - Category updated successfully.
-   `400`: Bad Request - Invalid input data format.
-   `401`: Unauthorized - Authentication credentials missing or invalid.
-   `403`: Forbidden - Insufficient permissions to perform the operation.
-   `404`: Not Found - Category not found.

<hr/>

### Delete Product Category Endpoint

- **URL**: `/api/category/{category_id}`
- **Method**: `DELETE`
- **Authentication**: JWT Token (Bearer Token)
- **Permissions**: Admin (IsAdmin)

#### Responses

- **Success (201)**: Category deleted successfully.
  - **Body**: `"Category deleted !!"`

- **Error (401)**: Unauthorized - User is not authenticated.
  - **Body**: `"Unauthorized"`

- **Error (403)**: Forbidden - User does not have sufficient permissions.
  - **Body**: `"Forbidden"`

- **Error (404)**: Not Found - Category not found.
  - **Body**: `"Category not found"`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/category/1';

fetch(url, {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
    }
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
```

#### Using JavaScript axios

```js
const axios = require('axios');

const url = '/api/category/1';

axios.delete(url, {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
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

Ensure proper error handling to manage responses for different scenarios like validation errors, authentication failures, and permission denials.

### Status Codes

-   `201`: Created - Category deleted successfully.
-   `401`: Unauthorized - Authentication credentials missing or invalid.
-   `403`: Forbidden - Insufficient permissions to perform the operation.
-   `404`: Not Found - Category not found.

Got it! Here’s an updated README.md description that includes the specific handling for `fetch` and `axios`.

<hr/>

### Create New Product Endpoint

- **URL**: `/api/products`
- **Method**: `POST`
- **Authentication**: JWT Token (Bearer Token)
- **Permissions**: Admin (IsAdmin)

#### Request Body

The request body can include the following JSON object:

```json
{
   "image": "<Image file>",
   "name": "product new name",
   "price": 100.0,
   "description": "product description",
   "stock": 50,
   "category_id": 1
}
```

In the case of `application/json` content type, the `image_url` field is used instead of `image` and contains the hyperlink to an image.

#### Responses

- **Success (201)**: Product created successfully.
  - **Body**: `"Product created successfully"`

- **Error (400)**: Bad Request - Invalid input data.
  - **Body**: List of validation errors or `"Failed to create product"`

- **Error (401)**: Unauthorized - User is not authenticated.
  - **Body**: `"Unauthorized"`

- **Error (403)**: Forbidden - User does not have sufficient permissions.
  - **Body**: `"Forbidden"`

- **Error (415)**: Unsupported Media Type - Allowed media types are 'application/json' or 'multipart/form-data'.
  - **Body**: `"Invalid content type"`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/products';
const data = new FormData();
data.append('image', imageFile); // imageFile is a file object
data.append('name', 'NewProduct');
data.append('price', 100.0);
data.append('description', 'Product description');
data.append('stock', 50);
data.append('category_id', 1);

fetch(url, {
    method: 'POST',
    headers: {
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
    body: data
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
```

#### Using JavaScript axios

```javascript
const axios = require('axios');

const url = '/api/products';
const data = new FormData();
data.append('image', imageFile); // imageFile is a file object
data.append('name', 'NewProduct');
data.append('price', 100.0);
data.append('description', 'Product description');
data.append('stock', 50);
data.append('category_id', 1);

axios.post(url, data, {
    headers: {
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE',
        'Content-Type': 'multipart/form-data'
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

Ensure proper error handling to manage responses for different scenarios like validation errors, authentication failures, and permission denials.

### Status Codes

-   `201`: Created - Product created successfully.
-   `400`: Bad Request - Invalid input data format.
-   `401`: Unauthorized - Authentication credentials missing or invalid.
-   `403`: Forbidden - Insufficient permissions to perform the operation.
-   `415`: Unsupported Media Type - Allowed media types are 'application/json' or 'multipart/form-data'.

<hr/>

### Get Product by ID Endpoint

- **URL**: `/api/products/{product_id}`
- **Method**: `GET`
- **Authentication**: None
- **Permissions**: None

#### Parameters

- **Path Parameter**:
  - `product_id` (integer, required): The ID of the product to retrieve.

#### Responses

- **Success (200)**: Product retrieved successfully.
  - **Body**: JSON object representing the product details.

  ```json
  {
      "category": {
          "id": 1,
          "name": "Play Station"
      },
      "description": "Gaming Console",
      "id": 1,
      "image_url": "static\\images\\Play Station 5\\82209737.jpg",
      "name": "Play Station 5",
      "price": 499.99,
      "stock": 99
  }
  ```

- **Error (400)**: Bad Request - Invalid input data.
  - **Body**: List of validation errors.

- **Error (404)**: Not Found - Product not found.
  - **Body**: `"Failed to grab product information"`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/products/1';

fetch(url, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
```

#### Using JavaScript axios

```javascript
const axios = require('axios');

const url = '/api/products/1';

axios.get(url, {
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

Ensure proper error handling to manage responses for different scenarios like invalid input data and product not found.

### Status Codes

- `200`: OK - Product retrieved successfully.
- `400`: Bad Request - Invalid input data format.
- `404`: Not Found - Product not found.

<hr/>

### Update Product Endpoint

- **URL**: `/api/products/{product_id}`
- **Method**: `PUT`
- **Authentication**: JWT Token (Bearer Token)
- **Permissions**: Admin (IsAdmin)

#### Parameters

- **Path Parameter**:
  - `product_id` (integer, required): The ID of the product to update.

#### Request Body

The request body can include the following JSON object:

```json
{
  "image": "<Image file>",
  "name": "Updated Product Name",
  "price": 150.0,
  "description": "Updated product description",
  "stock": 30,
  "category_id": 2
}
```

In the case of `application/json` content type, the `image_url` field is used instead of `image` and contains the hyperlink to an image.

#### Responses

- **Success (200)**: Product updated successfully.
  - **Body**: `"Product updated successfully"`

- **Error (400)**: Bad Request - Invalid input data.
  - **Body**: List of validation errors or `"Failed to update product"`

- **Error (401)**: Unauthorized - User is not authenticated.
  - **Body**: `"Unauthorized"`

- **Error (403)**: Forbidden - User does not have sufficient permissions.
  - **Body**: `"Forbidden"`

- **Error (404)**: Not Found - Product not found.
  - **Body**: `"Product not found"`

- **Error (415)**: Unsupported Media Type - Allowed media types are 'application/json' or 'multipart/form-data'.
  - **Body**: `"Invalid content type"`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/products/1';
const data = new FormData();
data.append('image', imageFile); // imageFile is a file object
data.append('name', 'Updated Product Name');
data.append('price', 150.0);
data.append('description', 'Updated product description');
data.append('stock', 30);
data.append('category_id', 2);

fetch(url, {
    method: 'PUT',
    headers: {
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
    body: data
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
```

#### Using JavaScript axios

```javascript
const axios = require('axios');

const url = '/api/products/1';
const data = new FormData();
data.append('image', imageFile); // imageFile is a file object
data.append('name', 'Updated Product Name');
data.append('price', 150.0);
data.append('description', 'Updated product description');
data.append('stock', 30);
data.append('category_id', 2);

axios.put(url, data, {
    headers: {
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE',
        'Content-Type': 'multipart/form-data'
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

Ensure proper error handling to manage responses for different scenarios like validation errors, authentication failures, and permission denials.

### Status Codes

- `200`: OK - Product updated successfully.
- `400`: Bad Request - Invalid input data format.
- `401`: Unauthorized - Authentication credentials missing or invalid.
- `403`: Forbidden - Insufficient permissions to perform the operation.
- `404`: Not Found - Product not found.
- `415`: Unsupported Media Type - Allowed media types are 'application/json' or 'multipart/form-data'.

<hr/>

### Delete Product Endpoint

- **URL**: `/api/products/{product_id}`
- **Method**: `DELETE`
- **Authentication**: JWT Token (Bearer Token)
- **Permissions**: Admin (IsAdmin)

#### Parameters

- **Path Parameter**:
  - `product_id` (integer, required): The ID of the product to delete.

#### Responses

- **Success (200)**: Product deleted successfully.
  - **Body**: `"Product Deleted"`

- **Error (400)**: Bad Request - Invalid input data.
  - **Body**: List of validation errors.

- **Error (401)**: Unauthorized - User is not authenticated.
  - **Body**: `"Unauthorized"`

- **Error (403)**: Forbidden - User does not have sufficient permissions.
  - **Body**: `"Forbidden"`

- **Error (404)**: Not Found - Product not found.
  - **Body**: `"Failed to delete product"`

### Example Usage

#### Using JavaScript Fetch

```javascript
const url = '/api/products/1';

fetch(url, {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
    }
})
.then(response => response.text())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
```

#### Using JavaScript axios

```javascript
const axios = require('axios');

const url = '/api/products/1';

axios.delete(url, {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE'
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

Ensure proper error handling to manage responses for different scenarios like invalid input data, authentication failures, and permission denials.

### Status Codes

- `200`: OK - Product deleted successfully.
- `400`: Bad Request - Invalid input data format.
- `401`: Unauthorized - Authentication credentials missing or invalid.
- `403`: Forbidden - Insufficient permissions to perform the operation.
- `404`: Not Found - Product not found.

<hr/>

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
- blacklisted_tokens.py: Black Listed Tokens model.

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

## File Handler Package

Explain the package (Amazon and localstorage are supported)

## Initializing Loggers in Flask

In Flask applications, initializing loggers ensures proper logging configurations throughout the application. Below are steps and examples for setting up logging in different parts of a Flask project.

### Setting Up Logging in the Flask Application

To configure logging for your Flask application, use the `setup_logging` function from `logger.py`.

#### Example in `app.py`

```python
from flask import Flask
from .logger import setup_logging

app = Flask(__name__)

# Setup Logger
setup_logging(app)

if __name__ == "__main__":
    app.run()
```

### Using Loggers in Flask Blueprints

When working with Flask Blueprints, initialize the logger in the `__init__.py` file of your Blueprint module.

#### File Structure Example

```
project_root/
    playstation/
        __init__.py
        app.py
        logger.py
        settings.py
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
```

#### Initializing Logger in `users/__init__.py`

```python
import logging
from logging import Logger
from playstation.settings import LOGGING_CONFIGURATION

# Get the logger
logger: Logger = logging.getLogger(LOGGING_CONFIGURATION["NAME"])
```

### Using Logger in Blueprint `app.py`

To use the logger in a Flask Blueprint (`app.py`), import it as follows:

```python
from . import logger
from flask import Blueprint, make_response, Response

example_api: Blueprint = Blueprint("example_api", __name__)

logger.error("An error has occurred")

@example_api.route("", methods=['GET'])
def example(*args, **kwargs) -> Response:

    try:
        # Some code that might raise an exception
        pass
    except Exception as e:
        logger.error(f"An error has occurred: {e}")
        return make_response("error", 400)
```

# Support My Work

If you find my free content and projects helpful, consider supporting me to enable more learning resources for the community. Your contributions will go towards creating new content and maintaining existing projects.

## How to Contribute

You can contribute by making a donation through PayPal:

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/Waheedkhaled?country.x=EG&locale.x=en_US)

Your generosity is greatly appreciated!

### Why Contribute?

By supporting this project, you help ensure the continued availability of free educational content and the development of new projects. Your contribution makes a meaningful impact on the community of learners.

Thank you for your support!