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
python manage.py
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

## Admin Package

The admin package contains modules related to the administration of the application, such as managing user permissions and authentication mechanisms.

## Applications Package

The applications package is divided into sub-packages, each responsible for different functional areas of the application, such as:

- pages: Manages the different pages of the application.
- users: Handles user-related operations.
- products: Manages product-related functionalities.
- orders: Deals with order processing and management.
- swagger: Contains configuration for API documentation using Swagger.

## Models Package

The models package defines the database models for the application. Each model represents a table in the database and includes:

- user.py: User model.
- products.py: Product model.
- orders.py: Order model.
- coupons.py: Coupon model.
- payments.py: Payment model.
- shipping_addresses.py: Shipping Address model.

## Serializers Package

Explain the package