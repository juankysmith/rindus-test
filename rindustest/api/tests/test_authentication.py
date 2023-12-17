from unittest.mock import call, patch, MagicMock
from django.test import TestCase
from rest_framework.exceptions import AuthenticationFailed

from api.authentication import BearerAuthentication

@patch('api.authentication.authentication')
class BearerAuthenticationTest(TestCase):
    def test_authenticate_no_auth(self, authentication_mock):
        authentication_mock.get_authorization_header.return_value =  ''
        self.assertEqual(BearerAuthentication().authenticate(MagicMock()), None)

    def test_authenticate_wrong_keyword(self, authentication_mock):
        authentication_mock.get_authorization_header.split.return_value =  [
            'wrong_keyword', 
            'blahblahblah'
        ]
        self.assertEqual(BearerAuthentication().authenticate(MagicMock()), None)

    def test_authenticate_auth_length_eq_one(self, authentication_mock):
        authentication_mock.get_authorization_header.return_value.split.return_value =  [b'Token']
        authentication_mock.exceptions.AuthenticationFailed = AuthenticationFailed
        with self.assertRaises(
            AuthenticationFailed, 
            msg="No credentials provided."
        ):
            BearerAuthentication().authenticate(MagicMock())

    def test_authenticate_auth_length_gt_two(self, authentication_mock):
        authentication_mock.get_authorization_header.return_value.split.return_value =  [
            b'Token', 'blahblahblah', 'blahblahblah'
        ]
        authentication_mock.exceptions.AuthenticationFailed = AuthenticationFailed
        with self.assertRaises(
            AuthenticationFailed, 
            msg="Token string should not contain spaces."
        ):
            BearerAuthentication().authenticate(MagicMock())

    @patch('api.authentication.BearerAuthentication.authenticate_credentials')
    def test_authenticate_happy_path(
        self, 
        authenticate_credentials_mock, 
        authentication_mock
    ):
        token = [
            b'Token', 
            b'fa4075b05dd38866081f2ad354a8702441b1470c'
        ]
        authentication_mock.get_authorization_header.return_value.split.return_value = token 
        BearerAuthentication().authenticate(MagicMock())
        
        self.assertEqual(authenticate_credentials_mock.call_count, 1)
        self.assertEqual(authenticate_credentials_mock.call_args_list[0], call(token[1].decode()))
