# PlayStation Store Backend

This project is about creating a playstation store which represents a simple E-commerce website using Flask as the backend technology.

- Later updates to this README.md where it will include installation of the project and setup and Cloud hosting of the project only.

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
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-blue)](https://pydantic-docs.helpmanual.io/)


## Main Flask Application

In this folder, you will find the Flask application assembled and ready to run. The application is divided into several folders and files for better organization and maintainability. Below is a breakdown of the directory structure and the purpose of each component.

### Directory Structure

```txt
project_root/
    app.py
    app.logs
    requirements.txt
    README.md // Overview about backend, Installation, Setup and hosting steps.
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
    playstation/
        __init__.py
        app.py
        README.md // Explains the Playstation Package
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



# Support My Work

If you find my free content and projects helpful, consider supporting me to enable more learning resources for the community. Your contributions will go towards creating new content and maintaining existing projects.

## How to Contribute

You can contribute by making a donation through PayPal:

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/Waheedkhaled?country.x=EG&locale.x=en_US)

Your generosity is greatly appreciated!

### Why Contribute?

By supporting this project, you help ensure the continued availability of free educational content and the development of new projects. Your contribution makes a meaningful impact on the community of learners.

Thank you for your support!