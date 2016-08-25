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
    # nullable = False should be place as last item in parentheses
    # photo_id = db.Column(db.ForeignKey('photos.id'), nullable=False)
    # location of comment is user zipcode translated into neighborhood name
    # location = db.Column(db.String(50), nullable=False)
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

#     photo = db.relationship('Photos', backref='users')
#     crime_data = db.relationship('CrimeData', backref='users')
#     police_district = db.relationship('PoliceDistrict', backref='users')
#     wallpost = db.relationship('WallPost', backref='users')
#     community = db.relationship('Community', backref='users')

#     def __repr__(self):
#         """Show info about user."""

#         return '<User user_id=%s user_name=%s first_name=%s last_name=%s e_mail=%s location=%s>' % 
#         (self.id, self.user_name, self.first_name, self.last_name, self.email, self.location)


# class WallPost(db.Model):
#     """Shows lists of posts"""

#     __tablename__ = 'wallposts'
#     wallpost_id = db.Column(autoincrement=True, primary_key=True)
#     user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
#     post_id = db.Column((db.ForeignKey('posts.id'), nullable=False) # FIX ME !!!!!!
#     wall_post = db.Column(db.String(150), nullable=False)

#     user = db.relationship('User', backref='wallposts')
#     post = db.relationship('Post', backref='wallposts')
#     photo = db.relationship('Photos', backref='wallposts')

#     # establish relationship between models and brands table 
#     # model = db.relationship('Model', backref='brands')

#     def __repr__(self):
#         """Show info about photos."""

#         return '<Wallpost wallpost_id=%s, user_id=%s post_id=%s wall_post=%s>'
#         (self.id, self.user_id, self.post_id, self.wall_post)


# class Photos(db.Model):
#     """Photos"""

#     __tablename__ = 'photos'
#     photo_id = db.Column(autoincrement=True, primary_key=True)
#     user_id = db.Column(db.ForeignKey('user.user_id'), nullable=False)
#     photo = db.Column(db.image_attachment('UserPicture')) # FIX ME !!!!!!
#     description = db.Column(db.String(50), nullable=True)
#     location = db.Column(db.String(50), nullable=False)
    
#     user = db.relationship('User', backref='photos')
#     post = db.relationship('Post', backref='photos')
#     wallpost = db.relationship('WallPost', backref='photos')

    
#     def __repr__(self):
#         """Show info about photos."""

#         return '<Photos photo_id=%s, user_id=%s photo=FIXME!!!! description=%s location=%s>' % 
#         (self.photo_id, self.user_id, self.photo, self.description, self.location)

# class CrimeData(db.Model):
#     """Crime Data"""

#     __tablename__ = 'crimedata'
#     crime_data_id = db.Column(autoincrement=True, primary_key=True)
#     type_of_crime= db.Column(db.String(50), nullable=False)
#     date = db.Column( #  FIX ME!!! does this need to be a datetime object???
#     day_of_week = db.Column(db.String(50), nullable=False)
#     time = db.Column(db.String(50), nullable=False) # in military time
#     # user_location is lat/long coordinates translated into neighborhood name
#     police_district = db.Column(db.ForeignKey('user.user_id'), nullable=False)

#     user = db.relationship('User', backref='crimedata')

#     # establish relationship between models and brands table 
#     # model = db.relationship('Model', backref='brands')

#     def __repr__(self):
#         """Show info about crime data."""

#         return '<Crime_Data crime_data_id=%s type_of_crime=%s date=%s day_of_week=%s time=%s police_district=%s>' % 
#         (self.crime_data_id, self.type_of_crime, self.date, self.day_of_week, self.time, self.police_district)

# class PoliceDistrict(db.Model):
#     """Police Districts"""

#     __tablename__ = 'police_districts'
#     police_district_id = db.Column(autoincrement=True, primary_key=True)
#     location = db.Column(db.String(50), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     user_id = db.Column(db.ForeignKey('users.id'),nullable=False 

#     user = db.relationship('User', backref='policedistricts')


#     def __repr__(self):
#         """Show info about police districts."""

#         return '<Police_District police_district_id=%s name=%s location=%s user_id=%s>' 
#         (self.police_district_id, self.name, self.location, self.user_id)



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

