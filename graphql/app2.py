from flask import Flask, jsonify, request
import graphene

app = Flask(__name__)

users = [
    {"id": 1, "name": "Abraham", "age": 30},
    {"id": 2, "name": "Isaac", "age": 40},
    {"id": 3, "name": "Jacob", "age": 50},
    {"id": 4, "name": "Rebecca", "age": 35}
]


# פונקציות עזר לחיפוש וסינון
def find_user_by_id(user_id):
    return next((user for user in users if user["id"] == user_id), None)


def find_users_by_name(name):
    return [user for user in users if user["name"] == name]


def filter_users_by_age(age):
    return [user for user in users if user["age"] == age]


def filter_users_by_age_range(min_age, max_age):
    return [user for user in users if min_age <= user["age"] <= max_age]


def find_users_by_name_substring(substring):
    return [user for user in users if substring.lower() in user["name"].lower()]



# ---------------- GraphQL API ----------------
class UserType(graphene.ObjectType):
    id = graphene.NonNull(graphene.Int)
    name = graphene.String()
    age = graphene.Int()


class Query(graphene.ObjectType):
    user_by_id = graphene.Field(UserType, user_id=graphene.Int(required=True))
    users_by_name = graphene.List(UserType, name=graphene.String(required=True))
    users_by_age = graphene.List(UserType, age=graphene.Int(required=True))
    users_by_age_range = graphene.List(UserType, min_age=graphene.Int(required=True), max_age=graphene.Int(required=True))
    users_by_name_substring = graphene.List(UserType, substring=graphene.String(required=True))

    def resolve_user_by_id(self, info, user_id):
        return find_user_by_id(user_id)

    def resolve_users_by_name(self, info, name):
        return find_users_by_name(name)

    def resolve_users_by_age(self, info, age):
        return filter_users_by_age(age)

    def resolve_users_by_age_range(self, info, min_age, max_age):
        return filter_users_by_age_range(min_age, max_age)

    def resolve_users_by_name_substring(self, info, substring):
        return find_users_by_name_substring(substring)


schema = graphene.Schema(query=Query)


def run_server():

    print("Running as GraphQL API")

    # נשתמש ב-GraphiQL לממשק אינטראקטיבי עבור GraphQL
    from flask_graphql import GraphQLView
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    # query example:
    """
    
    {
        userById(userId: 2) {
            id
            name
            age
        }
    }
    """

    # example query age range from 10 to 20
    """
    
    {
        usersByAgeRange(minAge: 10, maxAge: 20) {
            id
            name
            age
        }
    }
    """
    app.route('/graphql', methods=['POST'])(lambda: jsonify(schema.execute(request.json['query']).data))

    app.run(debug=True, port=5000)


if __name__ == "__main__":
    run_server()
