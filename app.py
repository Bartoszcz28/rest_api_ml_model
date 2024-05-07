
import pickle
import numpy as np
from flask import Flask, request, jsonify
from class_perceptron import *

# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route('/predict', methods=['GET','POST'])
def post_predict():
    if request.method == 'POST':
        data = request.get_json(force=True)
        sepal_length = float(data['sl'])
        petal_length = float(data['pl'])
        
    elif request.method == 'GET':
        sepal_length = float(request.args.get('sl'))
        petal_length = float(request.args.get('pl'))
    
    features = [sepal_length, petal_length]

    # Load pickled model file
    with open('model.pkl',"rb") as picklefile:
        model = pickle.load(picklefile)
        
    # Predict the class using the model
    predicted_class = int(model.predict(features))
    output = dict(features=features, predicted_class=predicted_class)
    
    # Return a json object containing the features and prediction
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
