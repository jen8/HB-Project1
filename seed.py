from model import connect_to_db, db, User, Post
from server import app


connect_to_db(app)

user1 = User(username='shacks', password='cat', first_name='Sarah', last_name='Hacks', zipcode=94123)
user2 = User(username='jhacks', password='cat', first_name='Jack', last_name='Hacks', zipcode=94123)
user3 = User(username='fhacks', password='cat', first_name='Frank', last_name='Hacks', zipcode=94123)


db.session.add(user1)
db.session.add(user2)
db.session.add(user3)



db.session.commit()