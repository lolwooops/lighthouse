# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle
import random


app = Flask(__name__)
api = Api(app)

filepath = 'C:/Users/Tim/Desktop/lighthouse/w7/d4/mini-project-IV/'

#everything not in pipeline

def log_transform(x):
    return np.log(x.astype(float) + 1)

# @app.route('/predict', methods=['POST'])
# def predict():
#     json_data = request.get_json()
#     df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
#     with open(filepath+'bestmodel.pickle', 'rb') as f:
#         best_model = pickle.load(f)
#         f.close()
#     predictions = best_model.predict_proba(df)

#     result = {
#         'prediction': list(predictions)
#     }
#     return result

# with open(filepath+'bestmodel.pickle', 'rb') as f:
#     best_model = pickle.load(f) 
# # model = pickle.load(open("bestmodel.pickle", "rb"))

class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        with open(filepath+'bestmodel.pickle', 'rb') as f:
            best_model = pickle.load(f)
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = best_model.predict_proba(df)
        # we cannot send numpt array as a result
        return res.tolist()
    
api.add_resource(Scoring, '/scoring')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)   
