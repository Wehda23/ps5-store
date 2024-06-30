# Application Package

The applications package is divided into sub-packages, each responsible for different functional areas of the application, such as:

- pages: Manages the different pages of the application.
- users: Handles user-related operations.
- products: Manages product-related functionalities.
- orders: Deals with order processing and management.
- swagger: Contains configuration for API documentation using Swagger.
- payments: Handles payment related Operations.
- shipping_addresses: Handles shipping addresses operations.

# File/Folder Structure.

```txt
applications/
            README.md // Explains how to interact with APIs and API end points
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
```

## Swagger Application

The Swagger Application provides interactive API documentation for the PlayStation Store Backend. It allows developers to explore and test the available API endpoints directly from the browser.

### Swagger Configuration

The Swagger UI is configured using the `flask_swagger_ui` package. Below is a summary of the configuration:

- **URL**: `/docs`
- **Swagger Config File**: `static/swagger_config.json`
- **Application Name**: "Play Station 5 Store"

![Swagger](https://i.postimg.cc/CL4jvR4s/Screenshot-58.png)

## Table of Contents

- [User Application](#user-application)
  - [User Registration API](#user-registration-api)
  - [Register User Endpoint](#register-user-endpoint)
  - [Login User Endpoint](#login-user-endpoint)
  - [Update User Endpoint](#update-user-endpoint)
  - [Refresh Token Endpoint](#refresh-token-endpoint)
  - [Logout Endpoint](#logout-endpoint)
- [Product Application](#product-application)
  - [Get All Product Categories Endpoint](#get-all-product-categories-endpoint)
  - [Create Product Category Endpoint](#create-product-category-endpoint)
  - [Update Product Category Endpoint](#update-product-category-endpoint)
  - [Delete Product Category Endpoint](#delete-product-category-endpoint)
  - [Create New Product Endpoint](#create-new-product-endpoint)
  - [Get Product By ID Endpoint](#get-product-by-id-endpoint)
  - [Update Product Endpoint](#update-product-endpoint)
  - [Delete Product Endpoint](#delete-product-endpoint)


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