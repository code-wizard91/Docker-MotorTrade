import unittest
import os

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import Users, Adverts
class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://ali:password@localhost/flaskapp' )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = Users(user_id=1, username='admin', first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        testuser = Users(user_id='2', username='test', first_name="test", last_name="user", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(testuser)
        db.session.commit()

    def tearDown(self):
        pass

class TestViews(TestBase):

    def test_home(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
