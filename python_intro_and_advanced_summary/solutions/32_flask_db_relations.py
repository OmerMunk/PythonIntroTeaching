# Topic Recap: Flask Models and Relationships with SQLAlchemy (Data Engineering Oriented)

# SQLAlchemy supports defining relationships between tables in a database using its ORM capabilities.
# In this session, we will create a Flask application that demonstrates one-to-many and many-to-many relationships.

# Step-by-Step Guide for Building a Flask Application with SQLAlchemy Models and Relationships

# Step 1: Set Up Flask and SQLAlchemy
# Install Flask and SQLAlchemy using pip if not already installed:
# pip install flask flask-sqlalchemy

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Step 2: Define Database Models with Relationships

# Example Models: User, Post, Tag
# - One-to-Many Relationship: User -> Posts (One user can have many posts)
# - Many-to-Many Relationship: Post <-> Tags (A post can have many tags, and a tag can be associated with many posts)

# User Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # One-to-Many relationship with Post

    def to_dict(self):
        return {"id": self.id, "name": self.name, "posts": [post.to_dict() for post in self.posts]}


# Post Model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User
    tags = db.relationship('Tag', secondary='post_tags', backref='posts',
                           lazy='dynamic')  # Many-to-Many relationship with Tag

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author_id": self.user_id,
            "tags": [tag.name for tag in self.tags]
        }


# Tag Model
class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


# Association Table for Many-to-Many Relationship between Post and Tag
post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
                     )


# Step 3: Create the Database and Tables
@app.before_first_request
def create_tables():
    db.create_all()


# Step 4: Define Routes for CRUD Operations with Relationships

# Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json:
        abort(400, description="Bad request")
    new_user = User(name=request.json['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


# Route: Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or 'title' not in request.json or 'content' not in request.json or 'user_id' not in request.json:
        abort(400, description="Bad request")
    user = User.query.get(request.json['user_id'])
    if user is None:
        abort(404, description="User not found")
    new_post = Post(title=request.json['title'], content=request.json['content'], author=user)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201


# Route: Add a tag to a post
@app.route('/posts/<int:post_id>/tags', methods=['POST'])
def add_tag_to_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        abort(404, description="Post not found")
    if not request.json or 'tag_name' not in request.json:
        abort(400, description="Bad request")
    tag_name = request.json['tag_name']
    tag = Tag.query.filter_by(name=tag_name).first()
    if not tag:
        tag = Tag(name=tag_name)
        db.session.add(tag)
    post.tags.append(tag)
    db.session.commit()
    return jsonify(post.to_dict())


# Step 5: Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)


# To run the Flask app, execute `python app.py` in your terminal.
# Access the application by opening a web browser and navigating to `http://127.0.0.1:5000/`.

# Explanation:
# 1. `User` model has a one-to-many relationship with the `Post` model.
# 2. `Post` model has a many-to-many relationship with the `Tag` model using an association table `post_tags`.
# 3. The routes demonstrate CRUD operations while handling relationships.

# 3 Easy Exercises

# Exercise 1 (Easy): Create a Route to Get All Posts by a User
# Explanation: Write a Flask route `/users/<int:user_id>/posts` that fetches all posts created by a user.
# Solution:
@app.route('/users/<int:user_id>/posts', methods=['GET'])
def get_posts_by_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify([post.to_dict() for post in user.posts])


# Example Input:
# Send a GET request to `/users/1/posts`.

# Example Output:
# [{"id": 1, "title": "Post Title", "content": "Post Content", "author_id": 1, "tags": []}]


# Exercise 2 (Easy): Create a Route to Get All Tags
# Explanation: Write a Flask route `/tags` that returns all tags in the database.
# Solution:
@app.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return jsonify([tag.to_dict() for tag in tags])


# Example Input:
# Send a GET request to `/tags`.

# Example Output:
# [{"id": 1, "name": "Python"}, {"id": 2, "name": "Flask"}]


# Exercise 3 (Easy): Create a Route to Delete a User
# Explanation: Write a Flask route `/users/<int:user_id>` to delete a user and all their associated posts.
# Solution:
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User and associated posts deleted successfully"})


# Example Input:
# Send a DELETE request to `/users/1`.

# Example Output:
# {"message": "User and associated posts deleted successfully"}


# 2 Medium Exercises

# Exercise 4 (Medium): Create a Route to Get All Posts with a Specific Tag
# Explanation: Write a Flask route `/posts/tag/<tag_name>` that returns all posts with a specific tag.
# Solution:
@app.route('/posts/tag/<tag_name>', methods=['GET'])
def get_posts_by_tag(tag_name):
    tag = Tag.query.filter_by(name=tag_name).first()
    if not tag:
        abort(404, description="Tag not found")
    posts = tag.posts.all()
    return jsonify([post.to_dict() for post in posts])


# Example Input:
# Send a GET request to `/posts/tag/Python`.

# Example Output:
# [{"id": 1, "title": "Flask with SQLAlchemy", "content": "Introduction to SQLAlchemy in Flask", "author_id": 1, "tags": ["Python"]}]


# Exercise 5 (Medium): Create a Route to Update a Post's Tags
# Explanation: Write a Flask route `/posts/<int:post_id>/tags` that updates the tags of a post.
# Solution:
@app.route('/posts/<int:post_id>/tags', methods=['PUT'])
def update_post_tags(post_id):
    post = Post.query.get(post_id)
    if post is None:
        abort(404, description="Post not found")
    if not request.json or 'tags' not in request.json:
        abort(400, description="Bad request")

    post.tags.clear()  # Clear existing tags
    for tag_name in request.json['tags']:
        tag = Tag.query.filter_by(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            db.session.add(tag)
        post.tags.append(tag)
    db.session.commit()
    return jsonify(post.to_dict())


# Example Input:
# Send a PUT request to `/posts/1/tags` with JSON body `{"tags": ["Python", "ORM"]}`.

# Example Output:
# {"id": 1, "title": "Post Title", "content": "Post Content", "author_id": 1, "tags": ["Python", "ORM"]}


# 1 Hard Exercise

# Exercise 6 (Hard): Create a Route to Search for Posts by Title and Tag
# Explanation: Write a Flask route `/posts/search` that takes query parameters `title` and `tag` and returns all posts that match the title pattern and have the specified tag.
# Solution:
@app.route('/posts/search', methods=['GET'])
def search_posts():
    title_pattern = request.args.get('title', '')
    tag_name = request.args.get('tag', '')

    query = Post.query
    if title_pattern:
        query = query.filter(Post.title.like(f"%{title_pattern}%"))
    if tag_name:
        query = query.join(Post.tags).filter(Tag.name == tag_name)

    posts = query.all()
    if not posts:
        abort(404, description="No posts found matching the criteria")

    return jsonify([post.to_dict() for post in posts])

# Example Input:
# Send a GET request to `/posts/search?title=Flask&tag=Python`.

# Example Output:
# [{"id": 1, "title": "Flask with SQLAlchemy", "content": "Introduction to SQLAlchemy in Flask", "author_id": 1, "tags": ["Python"]}]
