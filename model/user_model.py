
import mysql.connector
import json
from flask import request, make_response
from datetime import datetime, timedelta
import jwt

class user_model():
    def __init__(self):
        # connection establishment code

        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="mysql123",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("Error!!!")

    def user_getall_model(self):
        # querry execution code
        self.cur.execute( "SELECT * FROM users")
        result=self.cur.fetchall()
        print(result)
        # return "This is user_signup_model"
        # return result
        if len(result)>0:
            # return json.dumps(result)
            # return make_response({'payload':result}, 200)
            res=make_response({'payload':result}, 200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
        else:
            return make_response({"message":"No data Found"}, 204)
        
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        print(data)

        return make_response({"message":"User created succesfully"}, 201)
    

    # def user_update_model(self,data):
    #     self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id='{data['id']}'")
    #     if self.cur.rowcount>0:
    #         return "User updated succesfully"
    #     else:
    #         return "Nothing to update"

    def user_update_model(self, data):
        query = """ UPDATE users SET name = %s, email = %s, phone = %s, role = %s, password = %s WHERE id = %s """
        values = (
            data['name'],
            data['email'],
            data['phone'],
            data['role'],
            data['password'],
            data['id']
            )
        self.cur.execute(query, values)
        if self.cur.rowcount > 0:
            return make_response({"message":"User updated successfully"}, 201)
        else:
            return make_response({"message":"Nothing to update"}, 202)
        

    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"User deleted succesfully"}, 200)
        else:
            return make_response({"message":"No user available"}, 202)


    def user_patch_model(self, data,id):
        qry="UPDATE users SET "
        for key in data:
            qry+=f"{key}='{data[key]}',"
        qry= qry[:-1]+f" Where id={id}"
        self.cur.execute(qry)

        if self.cur.rowcount>0:
            return make_response({"message":"User updated succesfully"}, 200)
        else:
            return make_response({"message":"No user available"}, 202)


    def user_pagination_model(self,limit,page):
        page=int(page)
        limit=int(limit)
        start=(page*limit)-limit
        qry= f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        print(result)
        # return "This is user_signup_model"
        # return result
        if len(result)>0:
            # return json.dumps(result)
            # return make_response({'payload':result}, 200)
            res=make_response({'payload':result, 'page_no':page}, 200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
        else:
            return make_response({"message":"No data Found"}, 204)
        
    def user_upload_avatar_model(self,uid,filepath):
        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id={uid}")

        if self.cur.rowcount>0:
            return make_response({"message":"File uploaded succesfully"}, 200)
        else:
            return make_response({"message":"No user available"}, 202)


    def user_login_model(self, data):
        self.cur.execute(f"SELECT id, name, email, phone, avatar, role_id FROM users WHERE email='{data['email']}' and password='{data['password']}'")
        result=self.cur.fetchall()
        userdata=result[0]
        exp_time=datetime.now() + timedelta(minutes=15)
        exp_epoch_time=int(exp_time.timestamp()) #int to remove the decimal
        payload={
            "payload":userdata,
            "exp":exp_epoch_time
        }
        jwtoken=jwt.encode(payload, 'fiza'# encryption key
                           , algorithm="HS256")
        return make_response({"token":jwtoken}, 200)