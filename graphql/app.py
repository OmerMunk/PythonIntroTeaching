from flask import Flask, jsonify
# create a new venv
# install falsk
# install graphene
# pip install graphene

import graphene


# שלבים:
# ליצור query
# ליצור schema
# ליצור custom queries

#
# # query to return a string
# # 1. CREATING THR QUERY.
#
#
# class Query(graphene.ObjectType):
#     hello = graphene.String( # the return type is a string
#         name = graphene.Argument(graphene.String, default_value="World")
#     )
#
#     # resolve function
#     # def resolve_<FIELD_NAME>
#     def resolve_hello(self, info, name):
#         return f"Hello {name}"
#
#
#
# # CREATING THE SCHEMA
#
# schema = graphene.Schema(query=Query)
#
#
# # EXECUTE CUSTOM QUERIES USING THE SCHEMA
#
# # get 'hello' , and pass 'shalom'
#
# my_query = """
# {
#     hello(name: "Shalom")
# }
# """
#
#
# # excecute
# result = schema.execute(my_query)
#


class Book(graphene.ObjectType):
    id = graphene.NonNull(graphene.Int)
    title = graphene.String()
    author = graphene.String()


class Query(graphene.ObjectType):
    book = graphene.Field(Book)

    def resolve_book(self, info):
        return Book(id=1, title="Harry Potter", author="J. K. Rowling")


schema = graphene.Schema(query=Query)

app = Flask(__name__)


@app.route('/')
def root_source():
    my_query = """
        {
            book {
                id
                title
            }
        }
    """

    result = schema.execute(my_query)
    return jsonify(result.data)


if __name__ == '__main__':
    app.run(debug=True)
