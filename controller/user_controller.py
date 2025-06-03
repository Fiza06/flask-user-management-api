print("user_controller loaded")
from app import app
from flask import request, send_file
from model.user_model import user_model
from model.auth_model import auth_model
from datetime import datetime

obj=user_model()
auth=auth_model()

@app.route('/user/getall')
@auth.token_auth('/user/getall')
def user_getall_controller():
    # return "This is the signup operation"
    return obj.user_getall_model()
# print("Route /user/signup registered")

@app.route('/user/addone', methods=["POST"])
def user_addone_controller():
    # return "This is the user adding operation"
    return obj.user_addone_model(request.form)

@app.route('/user/update', methods=["PUT"])
def user_update_controller():
    # return "This is the update operation"
    return obj.user_update_model(request.form)


@app.route('/user/delete/<id>', methods=["DELETE"])
def user_delete_controller(id):
    # return "This is the update operation"
    return obj.user_delete_model(id)

@app.route('/user/patch/<id>', methods=["PATCH"])
def user_patch_controller(id):
    # return "This is the update operation"
    return obj.user_patch_model(request.args, id)

@app.route('/user/getall/limit/<limit>/page/<page>', methods=["GET"])
def user_pagination_controller(limit,page):
    # return "This is the update operation"
    return obj.user_pagination_model(limit,page)

@app.route('/user/<uid>/upload/avatar', methods=["PUT"])
def user_upload_avatar_controller(uid):
    # print(request.files) Its giving an immutable dictionary so to get the value we pass a key which here is 'avatar'.
    file = request.files['avatar']
    # file.save(f"uploads/{file.filename}")
    # return f"This is user upload avatar controller for {uid}"
    unique_filename  = str(datetime.now().timestamp()).replace(".","")
    fileNameSplit=file.filename.split(".")
    ext=fileNameSplit[len(fileNameSplit)-1]
    final_file = f"uploads/{unique_filename}.{ext}"
    file.save(final_file)
     
    return obj.user_upload_avatar_model(uid,final_file)


@app.route('/uploads/<filename>')
def user_getavatar_controller(filename):
    return send_file("uploads/1747913787494625.jpeg")

@app.route('/user/login', methods=["POST"])
def user_login_controller():
    return obj.user_login_model(request.form)


# import os
# print("user_controller.py path:", os.path.abspath(__file__))
  