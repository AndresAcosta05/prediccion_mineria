from flask import Flask, jsonify
from routes.prediction_routes import prediction
from routes.user_routes import user

app = Flask(__name__)
app.secret_key = '9FSSbRHjf1JbMA7mO0rcCZ4PPTMbJoGm'
app.register_blueprint(prediction)
app.register_blueprint(user)

@app.route('/')
def index():
    return jsonify({'Mensaje': 'Bienvenido a Flask'})


if __name__ == '__main__':
    app.run(debug=True)