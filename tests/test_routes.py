import unittest
import os
import pytest
from flask import abort, url_for, request
from flask_testing import TestCase
from sqlalchemy.exc import IntegrityError
from application import *
from application.models import *
class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
            SECRET_KEY='fee323f72238c94ce34302364eb0b21a',
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


    def tearDown(self):
        pass

    

class TestViews(TestBase):
    
    def test_create_user(self):
        """
        Here I test if the database will accept users by adding a test user
        """
        testuserr= Users(user_id='3', username='test3', first_name="test3", last_name="user3", email="test@user.com3", password="test20163")
        db.session.add(testuserr)
        db.session.commit()
        assert Users.query.count() == 1
    
    def test_sensor_name_unique(self):
        """
        Here I test to see if the DB will raise an error if we add two same users with the same user ID which it should
        """
        testuser1= Users(user_id='3', username='test3', first_name="test3", last_name="user3", email="test@user.com3", password="test20163")
        testuser2= Users(user_id='3', username='dsaddsa', first_name="tdsaas", last_name="dsada", email="dsada@dasdsad", password="acb")
        db.session.add(testuser1)
        db.session.add(testuser2)    
        with pytest.raises(IntegrityError):
            db.session.commit()


    def test_home(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_variant(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_login(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)
    def test_about(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    def test_account(self):
        """
        testing to see if the website gives access to accounts page when not logged in
        """
        response = self.client.get(url_for('account'))
        self.assertEqual(response.status_code, 302)
    def test_NewAdv(self):
        """
        testing to see if the website gives access to create new advert page when not logged in, it should redirect
        """
        response = self.client.get(url_for('new_advert'))
        self.assertEqual(response.status_code, 302)
    def test_logout(self):
        """
        testing to see if the website redirects when unlogged in users try to logout using /logout
        """
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 302)
    
    
    def test_advert(self):
        """
        testing to see if the website throws error when non users access /advert
        """
        response = self.client.get('/advert')
        self.assertEqual(response.status_code, 404)

    def test_New_advert(self):
        """
        testing to see if the website redirects to login when non users try to access create new advert page
        """
        response = self.client.get('/advert/new')
        self.assertEqual(response.status_code, 302)

    def test_update_advert(self):
        """
        testing to see if the website redirects to login when non users try to update a advert """
        response = self.client.get('/advert/1/update')
        self.assertEqual(response.status_code, 302)

    def test_existing_advert(self):
        """
        testing to see if non users can access non existant public adverts
        """
        response = self.client.get('/advert/1')
        self.assertEqual(response.status_code, 404)
    
    def test_delete_advert(self):
        """
        testing to see if non users can access non existant public adverts
        """
        response = self.client.get('/advert/1/delete')
        self.assertEqual(response.status_code, 405)


