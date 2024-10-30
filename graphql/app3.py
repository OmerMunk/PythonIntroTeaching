from flask import Flask, jsonify, request
import graphene as g
from flask_graphql import GraphQLView




app = Flask(__name__)

users = [
    {"id": 1, "name": "Shalom", "age": 30},
    {"id": 2, "name": "Pahshish", "age": 40},
    {"id": 3, "name": "Pahshish", "age": 42},
    {"id": 4, "name": "Rafi", "age": 35},
    {"id": 5, "name": "Sasson", "age": 50},
]


def find_user_by_id(user_id):
    filtered_users = [user for user in users if user["id"] == user_id]
    if filtered_users:
        return filtered_users[0]
    return None

def find_users_by_name(name):
    return [user for user in users if user["name"] == name]

def filter_users_by_age(age):
    return [user for user in users if user["age"] == age]

def filter_users_by_age_range(min_age, max_age):
    return [user for user in users if min_age <= user["age"] <= max_age]

def find_users_by_name_substring(substring):
    return [user for user in users if substring.lower() in user["name"].lower()]


class UserType(g.ObjectType):
    id = g.NonNull(g.Int)
    name = g.String()
    age = g.Int()


class Query(g.ObjectType):
    user_by_id = g.Field(UserType, user_id=g.Int(required=True))
    users_by_name = g.List(UserType, name=g.String(required=True))


    def resolve_user_by_id(self, info, user_id):
        return find_user_by_id(user_id)

    def resolve_users_by_name(self, info, name):
        return find_users_by_name(name)


schema = g.Schema(query=Query)


if __name__ == '__main__':
    app.add_url_rule('/graphql',
                     view_func=GraphQLView.as_view('graphql',
                                                   schema=schema,
                                                   graphiql=True))

    app.run(debug=True)