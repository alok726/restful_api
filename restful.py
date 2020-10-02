from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'alok'
api = Api(app)
jwt = JWT(app, authenticate, identity)



items = []


class Item(Resource):
    # @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    @jwt_required()
    def post(self, name):
        item = {'name': name, 'price': 100}
        items.append(item)
        return item, 201


class ItemList(Resource):
    # @jwt_required()
    def get(self):
        return {'items': items}


# api.add_resource(Student, '/student/

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run()
