from models.user_model import userModel

class userController:

    @classmethod
    def getUser(self, user):
        for dato in user:
            if not dato:
                return False
        response = userModel.login_user(user=user)
        return response
    
    @classmethod
    def cr_insert_user(self, user):
        for dato in user:
            if not dato:
                return False
        
        response = userModel.insert(user=user)
        return response
        