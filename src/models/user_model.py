from flask import jsonify
from config import Conecction

class userModel:

    @classmethod
    def login_user(self, user):
        try:
            with Conecction.getConecction().cursor() as cursor:
                sql = 'SELECT * FROM users WHERE us_user=%s AND us_password=%s'
                cursor.execute(sql, (user['usuario'], user['password']))
                return cursor.fetchone()
        
        except Exception as ex:
            print(ex)
            return False