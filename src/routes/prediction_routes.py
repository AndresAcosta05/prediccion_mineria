from flask import Blueprint, jsonify, request
from controllers.prediction_controller import predictionController
from flask_cors import cross_origin

prediction = Blueprint('Prediction', __name__)

@prediction.route('/prediction')
def index_prediction():
    return jsonify({'Mensaje': 'Bienvenido a flask prediccion'})

@prediction.route('/prediction/predict', methods=['POST'])
@cross_origin()
def prediction_predict():
    response = predictionController.cr_prediction_predict(request.json)
    return jsonify(response)