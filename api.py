from flask import Flask
from flask_restful import Resource, Api

app =Flask(__name__)
api =Api(app)

todos = {
    1: {"task": "write something", "desc": "write the code and explain."}
}

class ToDo(Resource):
    def get(self, id):
        return todos[id]



api.add_resource(ToDo ,'/todos/<int : id>')

if __name__ =='__main__':
    app.run(debug=True) 