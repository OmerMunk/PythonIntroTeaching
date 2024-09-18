# app.py
- import db
- import all the blueprint
- init a flask app
- app.config - sql database uri.
- db.init(app)
- with app.app_context():
  - db.create_all()
- with db.: 
- app.register al the blueprint
- app.run
- 

# db.py
- db = Flasksqlalchemy()


# Models /

## user model
- id primary key
- name string


## todo model
- id primary key
- task
- due date - datetime
- competed_at datetime / None
- isCompleted bool

(connect to user)



# BluePrints / Controllers / 

## todo blueprint (create, update, delete and etc...) prefix /todo
- POST /
- PUT /
- DELETE /

## user blueprint

## todos blueprint (get filtered by sort by) prefix /todos
- GET /?sortby=SHUBULU&filterby=SHUBULU
