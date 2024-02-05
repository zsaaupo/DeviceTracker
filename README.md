# Asset Tracking System Documentation

The Asset Tracking System is a Django-based web application designed to help companies track their corporate assets, manage employees, and monitor device assignments.


## Features

- Multi-company support
- Company administrators can add devices, employees, and assign devices.
- Employee users can view device information, assignment logs and assign devices.
- RESTful API for creating companies, employees, devices, and managing assignments.

## User Permissions
**Company User**
- Can add employees, add devices, and assign/return devices.

**Employee User**
- Can assign/return devices and view device information.


## Django Topics

- Django RESTful API
- Serializers
- User Groups


## How to Run

Clone the repository:

```bash
git clone https://github.com/zsaaupo/DeviceTracker
```

Create virtual environment

```bash
python -m venv venv

venv\scripts\activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Run
```bash
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

## 🚀 About Me
I'm a Software engineer...


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://zsaaupo.my.canva.site/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zsaaupo/)

## 🛠 Skills
Python, Django, REST framework, SQL, JavaScript, HTML, CSS, JAVA, Spring Boot...
