from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = API(app)

class add(Resource):
    def post(self):
        pull = request.get_json()
        x = int(pull['x'])
        y = int(pull['y'])
        summ = x+y
        ret = {
            'Message': summ,
            'Status code': 200
        }
        return jsonify(ret)

class subtract(Resource):
    def post(self):
        pull = request.get_json()
        x = int(pull['x'])
        y = int(pull['y'])
        diff = x-y
        ret = {
            'Message': diff,
            'Status code': 200
        }
        return jsonify(ret)

class multiply(Resource):
    def post(self):
        pull = request.get_json()
        x = int(pull['x'])
        y = int(pull['y'])
        multi = x*y
        ret = {
            'Message': multi,
            'Status code': 200
        }
        return jsonify(ret)

class divide(Resource):
    def post(self):
        pull = request.get_json()
        x = float(int(pull['x']))
        y = int(pull['y'])
        div = x/y
        ret = {
            'Message': div,
            'Status code': 200
        }
        if (int(pull['y'])==0):
            indiv = {
                "Message": "Indivisible",
            }
            return jsonify(indiv)
        else:
            return jsonify(ret)

api.add_resource(add, '/add')
api.add_resource(subtract, '/subtract')
api.add_resource(multiply, '/multiply')
api.add_resource(divide, '/divide')

if __name__ == '__main__':
    app.run(debug=True)
