# 🎮 PlayStation Store Backend

This project creates a PlayStation store representing a simple e-commerce website using Flask as the backend technology.

- Future updates will include detailed installation, setup, and cloud hosting instructions.

## 🌟 Introduction

The project includes the following features:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-blue)](https://pydantic-docs.helpmanual.io/)

## 📜 Table of Contents
1. [Introduction](#🌟-introduction)
2. [Main Flask Application](#🚀-main-flask-application)
3. [Create Virtual Environment](#🐍-create-virtual-environment)
4. [Run Application](#🏃-run-application)
5. [Database Schema](#🗄️-database-schema)
6. [Hosting with Nginx and Gunicorn](#🌐-hosting-with-nginx-and-gunicorn)
7. [Support My Work](#💖-support-my-work)

## 🚀 Main Flask Application

In this folder, you will find the Flask application assembled and ready to run. The application is divided into several folders and files for better organization and maintainability. Below is a breakdown of the directory structure and the purpose of each component.

### Directory Structure

```txt
project_root/
    app.py
    app.logs
    requirements.txt
    README.md // Provides an overview of the project, backend architecture, detailed installation instructions, setup guide, and hosting steps.
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
        README.md // Describes the purpose and functionality of the Playstation package, including key components and how they interact.
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
            README.md // Provides detailed documentation on API interactions, available endpoints, request and response formats, and usage examples.
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

## 🐍 Create Virtual Environment

If you are running this project in a development stage, it is advised to use a Python virtual environment.

- To create a virtual environment:

    ```bash
    python -m venv venv
    ```

- To activate the virtual environment:

    ```bash
    venv\Scripts\activate
    ```

## 🏃 Run Application

To run the application, you need to have Python installed on your machine.

- Install dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

- Run the application by executing the following command in your terminal:

    ```bash
    python app.py
    ```

## 🗄️ Database Schema

This project utilizes the following database schema to manage and organize data efficiently. The schema defines the structure, relationships, and constraints for the database tables.

![Database Schema](https://i.imghippo.com/files/GQdfW1717777832.png)

The diagram provides a visual representation of the tables, columns, and their relationships, ensuring a clear understanding of the data flow and organization within the system.


## 🌐 Hosting with Nginx and Gunicorn

To host the application using Nginx and Gunicorn, follow these instructions.

### Prerequisites

- Ensure you have a server running on DigitalOcean or a similar service.
- Install necessary software packages.

### Step 1: Install Gunicorn

```bash
pip install gunicorn
```

### Step 2: Create a Gunicorn Systemd Service

Create a file at `/etc/systemd/system/myproject.service` with the following content:

```ini
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=yourusername
Group=www-data
WorkingDirectory=/home/yourusername/myproject
Environment="PATH=/home/yourusername/myproject/venv/bin"
ExecStart=/home/yourusername/myproject/venv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

### Step 3: Start and Enable the Gunicorn Service

```bash
sudo systemctl start myproject
sudo systemctl enable myproject
```

### Step 4: Install Nginx

```bash
sudo apt update
sudo apt install nginx
```

### Step 5: Configure Nginx

Create a file at `/etc/nginx/sites-available/myproject` with the following content:

```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/yourusername/myproject/myproject.sock;
    }
}
```

Enable the file by creating a symlink:

```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```

### Step 6: Test Nginx Configuration and Restart

```bash
sudo nginx -t
sudo systemctl restart nginx
```

For a detailed guide, refer to this [DigitalOcean tutorial](https://dev.to/stefanie-a/how-to-deploy-a-flask-app-on-digitalocean-3ib7).

## 💖 Support My Work

If you find my free content and projects helpful, consider supporting me to enable more learning resources for the community. Your contributions will go towards creating new content and maintaining existing projects.

### How to Contribute

You can contribute by making a donation through PayPal:

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/Waheedkhaled?country.x=EG&locale.x=en_US)

Your generosity is greatly appreciated!

### Why Contribute?

By supporting this project, you help ensure the continued availability of free educational content and the development of new projects. Your contribution makes a meaningful impact on the community of learners.

Thank you for your support!