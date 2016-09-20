from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()



class Post(db.Model):
    """User Post."""

    __tablename__ = 'posts'
    # foreign key established to brand table to link tables together
    # if a table that has a single matching row in the second table, 
    # the first table has foreign key
    post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.user_id'), nullable=False)

    post = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    photo_id = db.Column(db.String(150), nullable=True)
    # photo_id = db.Column(db.ForeignKey('photos.id'), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=True)

    # establish relationship between posts and wallposts table 
    # wallpost = db.relationship('WallPost', backref='posts')
    
    
    # establish relationship between posts and photos table 
    # photos = db.relationship('Photos', backref='posts')

    def __repr__(self):
        """Show info about post."""

        return '<Post post_id=%d post=%s>' % (self.post_id, self.post)
        

        # return '<Post post_id=%s user_id=%s post=%s location=%s photo_id=%s' % (
        #     self.id, self.user_id, self.comment_id, self.location, self.photo_id)


class User(db.Model):
    """Users"""

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # user location is zipcode translated into neighborhood name
    zipcode = db.Column(db.Integer, nullable=False,)





##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///crime'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."

