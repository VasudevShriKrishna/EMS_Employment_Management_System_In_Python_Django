# EMS_Employment_Management_System_In_Python_Django

EMS is a Django-based web application for managing employee records with CRUD operations. 

Built using Python and PyCharm, it supports a clean admin interface and image handling via the Pillow library.

This system allows users to perform CRUD operations on employee records and provides an admin interface for centralized control.

🚀 Features
-> Add, edit, and delete employee details

-> View all employee records in a structured table

-> Admin panel for secure backend management

-> Responsive UI (optional Bootstrap support)

-> Built-in Django authentication for secure access

🛠️ Tech Stack
-> Backend: Python, Django

-> Frontend: HTML, CSS, Bootstrap (optional)

-> Database: SQLite (default with Django)

-> IDE: PyCharm / VS Code




STEP-BY-STEP: Clone the repository

1. Open the Project Folder in PyCharm
   
Open PyCharm,

Go to Folder > Open with PyCharm


2. Create a Virtual Environment in PyCharm

3. Install Django & Pillow Packages

4. Apply Migrations

5. Create a Superuser

6. Run the Server

7. **Ensure MySQL Server is Running**

* On **Windows**, open **Services** (press `Win + R`, type `services.msc`, press Enter), and look for:

  * `MySQL` or `MySQL80` or something similar.
* Make sure it's **Running**. If not, right-click it and choose **Start**.

Or run this in **Command Prompt**:

cmd - net start MySQL

If you're using XAMPP/WAMP, make sure **MySQL is started** in their control panel.

8. **Check MySQL Port**

Make sure MySQL is running on port `3306` (or whatever port you’ve configured in `settings.py` under `DATABASES`):

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',  # make sure this is correct
    }
}

9. **Check MySQLdb Installation**

You're using `MySQLdb`, which is part of `mysqlclient`. Make sure it's installed correctly:
pip install mysqlclient

If you have trouble installing it, you can try an alternative like `PyMySQL`:

pip install pymysql

Then in your `__init__.py` (inside your Django project directory), add:

import pymysql
pymysql.install_as_MySQLdb()

On Windows, a firewall or antivirus might block port `3306`. You can test if the port is open using:

telnet localhost 3306

If telnet is not installed, enable it or use another port testing tool.

✅ Summary

* 🔄 Start your MySQL service.
* 🔧 Check the `HOST` and `PORT` in your Django settings.
* 🔐 Ensure credentials (username/password) are correct.
* ✅ Confirm the correct DB driver is installed (`mysqlclient` or `pymysql`).
