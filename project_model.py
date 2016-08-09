class Comment(db.Model):
    """Comments."""

    __tablename__ = 'comments'
    # foreign key established to brand table to link tables together
    # if a table that has a single matching row in the second table, 
    # the first table has foreign key
    user_id = db.Column(db.ForeignKey('user.user_id'),nullable=False
    comment_id  = db.Column(autoincrement=True, primary_key=True)
    # comment_id doesn't need type, it uses the type from user.user_id?
    comment = db.Column(db.VARCHAR(150), nullable= False)
    # nullable = False should be place as last item in parentheses
    # location of comment is lat/long coordinates translated into neighborhood name
    location_of_comment = db.Column(db.VARCHAR(50), nullable=False)
    # establish relationship between models and brands table 
    # brand = db.relationship('Brand', backref='models')

    def __repr__(self):
        """Show info about comments."""

        return '<Comment user_id=%s comment_id=%s location_of_comment=%s' % (
            self.user_id, self.comment_id, self.location_of_comment)


class User(db.Model):
    """Users"""

    __tablename__ = 'users'
    # id = db.Column(SERIAL PRIMARY KEY)
    user_id = db.Column(autoincrement=True, primary_key=True)
    user_name = db.Column(db.VARCHAR(50), nullable=False)
    first_name = db.Column(db.VARCHAR(50), nullable=False)
    last_name = db.Column(db.VARCHAR(50), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False)
    # user_location is lat/long coordinates translated into neighborhood name
    user_location = db.Column(db.VARCHAR(50), nullable=False,)

    # establish relationship between models and brands table 
    # model = db.relationship('Model', backref='brands')

    def __repr__(self):
        """Show info about user."""

        return '<User user_id=%s user_name=%s first_name=%s last_name=%s e_mail=%s>' % 
        (self.user_id, self.user_name, self.first_name, self.last_name, self.email)


class Photos(db.Model):
    """Photos"""

    __tablename__ = 'photos'
    user_id = db.Column(db.ForeignKey('user.user_id'), nullable=False
    photo = db.Column(db.image_attachment('UserPicture')) # FIX ME !!!!!!
    photo_description = db.Column(db.VARCHAR(50), nullable=True)
    location_of_photo = db.Column(db.VARCHAR(50), nullable=False)
    photo_id = db.Column(autoincrement=True, primary_key=True)

    # establish relationship between models and brands table 
    # model = db.relationship('Model', backref='brands')

    def __repr__(self):
        """Show info about photos."""

        return '<Photos photo_id=%s, user_id=%s photo=FIXME!!!! photo_description=%s 
                last_name=%s location_of_photo=%s>' % 
        (self.photo_id, self.user_id, self.photo, self.photo_description, 
        self.location_of_photo)

class CrimeData(db.Model):
    """Crime Data"""

    __tablename__ = 'crimedata'
    type_of_crime= db.Column(db.VARCHAR(50), nullable=False)
    date = db.Column( #  FIX ME!!! does this need to be a datetime object???
    day_of_week = db.Column(db.VARCHAR(50), nullable=False)
    time = db.Column(db.VARCHAR(50), nullable=False) # in military time
    # user_location is lat/long coordinates translated into neighborhood name
    police_district = db.Column(db.VARCHAR(50), nullable=False,)

    # establish relationship between models and brands table 
    # model = db.relationship('Model', backref='brands')

    def __repr__(self):
        """Show info about crime data."""

        return '<Crime_Data type_of_crime=%s date=%s day_of_week=%s time=%s police_district=%s>' % 
        (self.type_of_crime, self.date, self.day_of_week, self.time, self.police_district)





