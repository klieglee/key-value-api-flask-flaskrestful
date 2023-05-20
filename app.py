from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

storage_file = 'storage.data'

class KeyValueResource(Resource):
    def get(self):
        storage = load_storage()
        return storage

    def post(self):
        key = request.form.get('key')
        value = request.form.get('value')

        if not key or not value:
            return {'error': 'Key or value not provided'}, 400

        storage = load_storage()
        if key in storage:
            storage[key].append(value)
        else:
            storage[key] = [value]
        save_storage(storage)
        return {key: storage[key]}

class KeySearchResource(Resource):
    def get(self, key):
        storage = load_storage()
        if key in storage:
            return {key: storage[key]}
        else:
            return {'error': 'Key not found'}, 404

def load_storage():
    try:
        with open(storage_file, 'r') as file:
            storage = json.load(file)
    except FileNotFoundError:
        storage = {}
    return storage

def save_storage(storage):
    with open(storage_file, 'w') as file:
        json.dump(storage, file)

@app.route('/')
def homepage():
    return '''
    <h1>Hranilishe Key-Value</h1>
    <p>Prototip API hranilishya key-value.</p>
    <p>--------------------------------------------</p>
    <p>Poluchiti vse dannie hranilisha WEB</p>
    <p>http://hostname:port/api/v1/storage/json/all</p>
    <p>--------------------------------------------</p>
    <p>Poluchiti vse dannie hranilisha CURL</p>
    <p>curl -i -X GET http://hostname:port/api/v1/storage/json/all</p>
    <p>--------------------------------------------</p>
    <p>Poluchiti dannie hranilisha po kluchu WEB</p>
    <p>http://hostname:port/api/v1/storage/json/read/<key></p>
    <p>--------------------------------------------</p>
    <p>Poluchiti dannie hranilisha po kluchu CURL</p>
    <p>curl -i -X GET http://hostname:port/api/v1/storage/json/key1</p>
    <p>--------------------------------------------</p>
    <p>Dobaviti dannie v hranilishe hranilisha WEB</p>
    <p>curl -i -X POST -d "key=key1&value=value1 http://hostname:port/api/v1/storage/json/all</p>
    '''

api.add_resource(KeyValueResource, '/api/v1/storage/json/all')
api.add_resource(KeySearchResource, '/api/v1/storage/json/read/<string:key>')

if __name__ == '__main__':
    app.run(debug=True)
