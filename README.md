# flask-user-management-api
A Flask-based REST API for user management, supporting CRUD operations, JWT authentication, role-based access, file uploads, and pagination — designed as a scalable backend for web or mobile applications.


A lightweight Flask REST API for managing users, featuring:
✅ User CRUD (Create, Read, Update, Delete)  
✅ JWT-based login and authentication  
✅ Role-based access control  
✅ File uploads (user avatars)  
✅ Pagination support

## Setup

1️⃣ Clone the repo 

git clone [https://github.com/yourusername/flask-user-management-api.git](https://github.com/yourusername/flask-user-management-api.git)
cd flask-user-management-api


2️⃣ Create a virtual environment  

python3 -m venv venv
source venv/bin/activate


3️⃣ Install dependencies  

pip install -r requirements.txt



4️⃣ Set up your MySQL database (`flask_tutorial`) with a `users` table

5️⃣ Run the app  

python app.py

## Main Endpoints

- `GET /user/getall` — Get all users  
- `POST /user/addone` — Add a new user  
- `PUT /user/update` — Update user  
- `DELETE /user/delete/<id>` — Delete user  
- `PATCH /user/patch/<id>` — Partially update user  
- `POST /user/login` — Login (returns JWT)  
- `PUT /user/<uid>/upload/avatar` — Upload avatar  
- `GET /uploads/<filename>` — Retrieve uploaded avatar

## Dependencies

Flask, mysql-connector-python, PyJWT
