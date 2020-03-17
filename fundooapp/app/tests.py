import requests
import json
import os
BASE_URL = 'http://127.0.0.1:8000'


class TestCasesForRegistration:

    def test_username_email_password_all_details_given(self):
        ENDPOINT = '/register/'
        url = BASE_URL + ENDPOINT
        data = {"email": "abhik.srivastava10003gmail.com", "password": "admin@123", "username": "Tom Singh Hanks"}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url=url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 201

    def test_username_not_given(self):
        ENDPOINT = '/register/'
        url = BASE_URL + ENDPOINT
        data = {'email': 'abhik.srivastava10003@gmail.com', 'password': 'admin@123'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 500

    def test_email_not_given(self):
        ENDPOINT = '/register/'
        url = BASE_URL + ENDPOINT
        data = {'username': 'annanya', 'password': 'admin@123'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 500

    def test_password_not_given(self):
        ENDPOINT = '/register/'
        url = BASE_URL + ENDPOINT
        data = {'username': 'Jazz', 'email': 'abhik.srivastava@gmail.com'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 500


class TestCasesForLogin:

    def test_email_username_all_details_given(self):
        ENDPOINT = '/login/'
        url = BASE_URL + ENDPOINT
        data = {"username": "abhik", "password": "admin@123"}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code

    def test_username_not_given(self):
        ENDPOINT = '/login/'
        url = BASE_URL + ENDPOINT
        data = {'password': 'admin@123'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code

    def test_password_not_given(self):
        ENDPOINT = '/login/'
        url = BASE_URL + ENDPOINT
        data = {'username': 'abhi'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code


class TestCasesForResetForgotPassword:

    def test_username_password_all_details_given(self):
        ENDPOINT = '/reset/'
        url = BASE_URL + ENDPOINT
        data = {'email': 'abhik.srivastava10003@gmail.com', 'username': 'abhik'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code

    def test_username_not_given(self):
        ENDPOINT = '/reset/'
        url = BASE_URL + ENDPOINT
        data = {'email': 'abhik.srivastava@gmail.com'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 500

    def test_email_not_given(self):
        ENDPOINT = '/reset/'
        url = BASE_URL + ENDPOINT
        data = {'username': 'abhik'}
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 500
