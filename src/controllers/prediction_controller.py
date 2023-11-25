from models.prediction_model import predictionModel

class predictionController:

    @classmethod
    def cr_prediction_predict(cls, data):
        for dato in data:
            if not dato:
                return False
        
        response = predictionModel().md_prediction_predict(data=data)
        return response
        
