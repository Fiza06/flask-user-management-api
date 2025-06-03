
from functools import wraps
import mysql.connector
import json
from flask import request, make_response
import jwt
import re # regular expression module to check if string is in a specific format etc.

class auth_model():
    def __init__(self):
        # connection establishment code

        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="mysql123",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("Error!!!")

    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func) # if we use @auth.token_auth multiple times and then func gets override so we use this decorator
            def inner2(*args):

                endpoint=request.url_rule
                authorization=request.headers.get("Authorization")
                if re.match("Bearer *([^ ]+) *$", authorization, flags=0):
                    token=authorization.split(" ")
                    try:
                        jwtdecoded=jwt.decode(token, "fiza", algorithms="HS256")
                    except:
                        return make_response({"ERROR": "TOKEN EXPIRED"}, 401)
                    role_id=jwtdecoded['payload']['role_id']
                    self.cur.execute(f"roles FROM accessibility_view WHERE endpount='{endpoint}'")
                    result=self.cur.fetchall()
                    if len(result)>0:
                        allowed_roles=json.loads(result[0]['roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({"ERROR":"INVALID ROLE"}, 404)
                    else:
                        return make_response({"ERROR":"UNNOWN ENDPOINT"}, 404)
                else:
                    return make_response({"ERROR":"INVALID TOKEN"}, 401)

            return inner2
        return inner1