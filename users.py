import sqlite3

from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        connection.close()

        if row:
            user = cls(*row)
        else:
            user = None

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        connection.close()

        if row:
            user = cls(*row)
        else:
            user = None

        return user


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This filed cannot be blank")

    def post(self):
        data = UserRegistration.parser.parse_args()
        print('User Registration', data)
        if User.find_by_username(data['username']) is not None:
            return {'message': f"A user with the name {data['username']} already exists"}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "user created successfully"}


User.find_by_username("Golu")

