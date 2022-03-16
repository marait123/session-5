from email import header
from http.client import ImproperConnectionState
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import Greeting, setup_db, db
from app import create_app
# TODO:
# make sure you create a database named hello_test in psql
database_name = "greetingtest"
database_path = 'postgresql://postgres:123456@localhost:5432/{}'.format(
    database_name)

admin_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlN6RTdwU0ZUSEJMTENIa2twQldYcCJ9.eyJpc3MiOiJodHRwczovL2hlcmZ5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDYwNjE3NjQ5OTk2MzM2MTE2NSIsImF1ZCI6IkdyZWV0aW5nQXBpIiwiaWF0IjoxNjQ3NDI5NDE3LCJleHAiOjE2NDc1MTU4MTcsImF6cCI6InpQRk8zN1RzOEF3TEJoVnQ5cVpQdHVxeXZmWWo0OVQ3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Z3JlZXRpbmdzIiwiZ2V0OmdyZWV0aW5ncy1kZXRhaWwiLCJwb3N0OmdyZWV0aW5ncyJdfQ.ZvQ3oivFTl7EVJrmO5NWzyzWNTPtgyltRhtP4uXDHwlV9AR558rbkXWKjnAaXFz3jljRbBWySsCyChI8bFqOp5OvRYBH03EvvURUZHPWEeH12whdV7Whf4gbkJRyv4doe3x8URJkV7aYU0pOGZAkRauHqlIUYj3UK6y0uHu0QuVdSAgAlyJp8WkCvuQ4MIDk7ZEGVzHkGRUExV7_JZv5ZAlkf1MkPtAHqfoRuAjRLDkQM2cQTDiwiWZxemPMDYX6iE-7IglEE5cMWRL3E35tGBZicgGZZ7bGKfE8di6CET7MbNzCDmJ2a-BLywPu1hXV9iTQpxcWP2-kgY7f9kA1gQ"
greeter_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlN6RTdwU0ZUSEJMTENIa2twQldYcCJ9.eyJpc3MiOiJodHRwczovL2hlcmZ5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDYwNjE3NjQ5OTk2MzM2MTE2NSIsImF1ZCI6IkdyZWV0aW5nQXBpIiwiaWF0IjoxNjQ3NDM5MzQ5LCJleHAiOjE2NDc1MjU3NDksImF6cCI6InpQRk8zN1RzOEF3TEJoVnQ5cVpQdHVxeXZmWWo0OVQ3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Z3JlZXRpbmdzIl19.X6jOMKOYhsxBF2DzmU3kn7Mz639g72epHbBmatGbdSRehMwNDQrypZXgOW0M4MmXVclYGFSC1s4QLcn4hnl81zksj_AfTjzDrAQdGpR4ZPKuKY4VXVHGCzYYj11saA7Jow3pmDhKomSZ-XsCgrX2nyoP7gAJnphZlbwnEsRD1mhWZlOoaHVnwE8RGE-wNb9HxXHZkGAbCv6-0w13VAk_k8Xd702KJSiLQFyy_g8Xig37DO_uc78zd6j3wnAJH12nhYsP41nS9xTgvOn1jasfCfn1kDHEEx2AtvsFaJbF4qFo9F4D5pmfXD_EAQxU5sBhSFNo3sISCKlmUgvef_8jbQ"


greetings = [{'lang': 'en', 'greeting': 'hello'},
             {'lang': 'es', 'greeting': 'Hola'},
             {'lang': 'ar', 'greeting': 'مرحبا'},
             {'lang': 'ru', 'greeting': 'Привет'},
             {'lang': 'fi', 'greeting': 'Hei'},
             {'lang': 'he', 'greeting': 'שלום'},
             {'lang': 'ja', 'greeting': 'こんにちは'}]


class GreetingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app.
            it is run before each test
        """
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        # each flask app has a context that includes all of the apps configuration like database, password, etc
        with self.app.app_context():
            # self.db = SQLAlchemy()
            self.db = db
            self.db.init_app(self.app)
            # clean the database beforehand
            self.db.drop_all()
            self.db.session.commit()

            # create all tables
            self.db.create_all()
            self.db.session.commit()

        with self.app.app_context():
            # insert the categories
            for greeting in greetings:
                cat = Greeting(**greeting)
                self.db.session.add(cat)
                self.db.session.commit()

    # in case you want to clean the database after each request
    def tearDown(self):
        """Executed after each test"""
        # with self.app.app_context():
        #     # clean the database beforehand
        #     self.db.drop_all()
        #     self.db.session.commit()
        pass

    # testing the greetings
    def test_get_greetings_ok(self):
        # print('hello')
        headers = {
            'Authorization': 'Bearer {}'.format(greeter_token)
        }
        print('hello test_get_greetings_ok')

        res = self.client().get('/greetings', headers=headers)  # res is of a type stream
        # print(res.data) # res.data is a of type string of characters
        # data is a of type string of characters
        new_greeetings = json.loads(res.data)
        # print(new_greeetings)
        self.assertEqual(res.status_code, 200)

    # test getting one greeting
    def test_one_greeting_ok(self):
        print('hello test_one_greeting')
        headers = {
            'Authorization': 'Bearer {}'.format(greeter_token)
        }
        res = self.client().get(f'/greetings/en', headers=headers)
        # print("res " , res)
        new_greeting = json.loads(res.data)
        # print("new_greeting ",new_greeting)
        self.assertEqual(res.status_code, 200)

        self.assertEqual(new_greeting["greeting"]
                         ['greeting'], greetings[0]["greeting"])

    # test getting one greeting

    def test_one_greeting_401(self):
        print('hello test_one_greeting_404')
        res = self.client().get(f'/greetings/en')
        # print("res " , res)
        new_greeting = json.loads(res.data)
        # print("new_greeting ",new_greeting)
        self.assertEqual(res.status_code, 401)

    def test_one_greeting_404(self):
        print('hello test_one_greeting_404')
        headers = {
            'Authorization': 'Bearer {}'.format(greeter_token)
        }
        res = self.client().get(f'/greetings/notfound', headers=headers)
        # print("res " , res)
        new_greeting = json.loads(res.data)
        # print("new_greeting ",new_greeting)
        self.assertEqual(res.status_code, 404)

        # self.assertEqual(new_greeting["greeting"]['greeting'], greetings[0]["greeting"])

    # test getting one greeting

    def test_create_greeting_ok(self):
        print('hello test_create_greeting_ok')
        headers = {
            'Authorization': 'Bearer {}'.format(admin_token)
        }
        res = self.client().post(f'/greetings', headers=headers,
                                 json=dict(lang="french", greeting="bonjour"))
        print("res ", res)
        print("res.data ", res.data)
        new_greeting = json.loads(res.data)
        # print("new_greeting ",new_greeting)
        self.assertEqual(res.status_code, 201)

    def test_create_greeting_403(self):
        print('hello test_create_greeting_40')
        headers = {
            'Authorization': 'Bearer {}'.format(greeter_token)
        }
        res = self.client().post(f'/greetings', headers=headers,
                                 json=dict(lang="french", greeting="bonjour"))

        # print("new_greeting ",new_greeting)
        self.assertEqual(res.status_code, 403)

    # TODO: implement a test case to test getting one beautiful greeting
    def test_beautiful_greeting(self):
        print('hello test_beautiful_greeting')

        self.assertEqual(200, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
