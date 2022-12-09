from flask import Flask
from flask_restful import Api, Resource #importing modules

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource): #resource will have few different methods that we can override in it
    def get(self):
        return {"data":"Hello World"} 

api.add_resource(HelloWorld, "/helloworld")     #register as a resource

if __name__ == "__main__":
    app.run(debug=True) #starts our application



