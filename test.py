import json
from unittest import TestCase
from model import Post, User, connect_to_db, db
from server import app



class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_display_post(self):
        """Test display post page."""

        result = self.client.get("/display_post")
        self.assertIn("Select a neighborhood", result.data)




class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        # connect_to_db(app, "postgresql:///crime")

        # Create tables and add sample data
        # db.create_all()
        # example_data()

    # def tearDown(self):
    #     """Do at end of every test."""

    #     db.session.close()
    #     db.drop_all()

    def test_make_post_page(self):
        """Test make posts page."""

        # go to make posts page and see if "Hello" is there
        result = self.client.get("/make_post")
        self.assertIn("Hello", result.data)



    def test_login(self):
        """Test login page."""
        # log in with user_id "shacks" and password "cat"
        # also check in "password" is on login page
        result = self.client.post("http://localhost:5000/",
                                  data={"user_id": "shacks", "password": "cat"},
                                  follow_redirects=True)
        self.assertIn("Select a neighborhood", result.data)





if __name__ == "__main__":
    import unittest
    connect_to_db(app)

    unittest.main()


