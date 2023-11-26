from flask import jsonify
from config import Conecction

class userModel:

    @classmethod
    def login_user(self, user):
        try:
            with Conecction.getConecction().cursor() as cursor:
                sql = 'SELECT * FROM users WHERE us_user=%s AND us_password=%s'
                cursor.execute(sql, (user['usuario'], user['contraseña']))
                return cursor.fetchone()
        
        except Exception as ex:
            print(ex)
            return False
    
    @classmethod
    def insert(self, user):
        connection = Conecction.getConecction()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO users(document, name, second_name, lastname, second_lastname, email, us_user, us_password, phone, type_user) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (user['document'], user['name'], user['second_name'], user['lastname'], user['second_lastname'], user['email'], user['us_user'], user['us_password'], user['phone'], 'USER'))
                connection.commit()
                return True

        except Exception as ex:
            print(ex)
            return False