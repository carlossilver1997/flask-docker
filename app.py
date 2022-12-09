from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return { "message": "hello world" }

api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)