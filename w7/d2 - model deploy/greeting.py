# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

# Create an application:
app = Flask(__name__)

# Create an API from the application:
api = Api(app)

# Now that our API has been created, we need to add an endpoint. 
# We can do that by creating a class with the name Greet (any 
# other name will work as well). This class must inherit properties 
# from the Resources class from the flask_restful module.

class Greet(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('name', type=str)

        # parse 'name'
        name = parser.parse_args().get('name')

        if name:
            greeting = f'Hello {name}!'
        else:
            greeting = 'Hello person without name!'

        # make json from greeting string 
        return jsonify(greeting=greeting)


# The class Greet contains only one method – get. This time the naming 
# convention is strict (we can use only HTTP request methods: get, post, 
# put, ...). Inside the get method, we initialize RequestParser() 
# which allows us to parse optional arguments. We create only one 
# optional argument name as a string type. In the variable name, we 
# store an argument value that was passed by calling our API. If the 
# user doesn't pass the argument name in an API call the value of the 
# variable is NULL. We also create different greetings based on the 
# value in the name variable.

# Now that we have our class created, we need to assign an endpoint. 
# The functionality of the Greet class will be available in the /greet endpoint.

# assign endpoint
api.add_resource(Greet, '/greet',)

# The last thing to do is to create an application run when the file 
# greeting_api.py is called directly (not imported as a module from another 
# script).

if __name__ == '__main__':
    app.run(debug=True)

# Run the API by opening the command line and type python greeting_api.py.