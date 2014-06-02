#coding: utf-8
from mock import patch
import json
import os

from django.test import TestCase
from django.contrib.auth import get_user_model, SESSION_KEY
from django.core import mail

from mail import send_generic_mail
from access import factories
from access.changeUserPassword import ChangeUserPassword
User = get_user_model()


class AccessAuthorizationDjangoTest(TestCase):
    fixtures = ['basic_auth.yaml']

    def test_access_login_by_domain(self):
        ret = self.client.get('/', follow=True)
        self.assertEquals(ret.status_code, 200, 'Wrong status code.')

    def test_access_login_by_address(self):
        ret = self.client.get('/access/login')
        self.assertEquals(ret.status_code, 200, 'Wrong status code.')

    def test_access_logout_by_address(self):
        ret = self.client.get('/access/logout', follow=True)
        self.assertEquals(ret.status_code, 200, 'Wrong status code.')

    def test_login_authorized(self):
        ret = self.client.post('/access/login',
            {'username': 'marcel', 'password': 'admin'}, follow=True)
        self.assertEquals(ret.status_code, 200, 'Wrong status code.')
        self.assertFalse('error_msg' in ret.context)

    def test_login_not_authorized(self):
        ret = self.client.post('/access/login',
            {'username': 'admin', 'password': 'ssss'})
        self.assertEquals(ret.status_code, 200, 'Wrong status code.')
        self.assertTrue('error_msg' in ret.context)

    @patch('access.views.authenticate')
    def test_login_django_autenticate_mock(self, m_authenticate):

        m_authenticate.return_value = None

        ret = self.client.post('/access/login',
            {'username': 'admin', 'password': 'admin'},
         follow=True)

        self.assertTrue('error_msg' in ret.context)

    @patch('access.views.authenticate')
    def test_calls_authenticate_with_assertion_from_post(
        self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/access/login',
            {'username': 'admin', 'password': 'admin'})
        mock_authenticate.assert_called_once_with(username='admin',
            password='admin')

    @patch('access.views.authenticate')
    def test_gets_logged_in_session_if_authenticate_returns_a_user(
        self, mock_authenticate):
        user = User.objects.get(email='leandroc@inatel.br')
        mock_authenticate.return_value = user
        user.backend = ''
        self.client.post('/access/login',
            {'username': 'marcel', 'password': 'admin'})
        self.assertEqual(self.client.session[SESSION_KEY], user.pk)

    @patch('access.views.authenticate')
    def test_does_not_get_logged_in_if_authenticate_returns_None(
        self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/access/login',
            {'username': 'adasmin', 'password': 'admin'})
        self.assertNotIn(SESSION_KEY, self.client.session)


class UserHandlerTest(TestCase):
    def test_get_list(self):
        factories.UserFactory.create(
            username="usertest",
            email='usertest@sodexoapp.com')

        ret = self.client.get('/access/user')

        self.assertEquals(ret.status_code, 200,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        content = json.loads(ret.content)
        self.assertEquals(content.get('total'), 1)

        user = content.get('result')[0]
        self.assertEquals(user.get('username'), 'usertest')
        self.assertEquals(user.get('email'), 'usertest@sodexoapp.com')

    def test_get_one(self):
        user = factories.UserFactory.create(
            username="userfake",
            email='userfake@sodexoapp.com')

        ret = self.client.get('/access/user/' + str(user.id))

        self.assertEquals(ret.status_code, 200,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        user = json.loads(ret.content).get('result')
        self.assertEquals(user.get('username'), 'userfake')
        self.assertEquals(user.get('email'), 'userfake@sodexoapp.com')

    def test_get_allowed_fields(self):
        factories.UserFactory.create(
            id=1,
            username="usertest",
            email='usertest@sodexoapp.com')

        ret = self.client.get('/access/user/1')

        self.assertEquals(ret.status_code, 200,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        self.assertEqual(json.loads(ret.content)['result'], {
                u"username": u"usertest",
                u"email": u"usertest@sodexoapp.com",
                u"id": 1})

    def test_get_one_not_found(self):
        factories.UserFactory.create(
            id=1,
            username="usertest",
            email='usertest@sodexoapp.com')
        ret = self.client.get('/access/user/2')

        self.assertEquals(ret.status_code, 404,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        self.assertEquals(ret.content, 'Not found')

    def test_get_list_empty(self):
        ret = self.client.get('/access/user')

        self.assertEquals(ret.status_code, 200,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        content = json.loads(ret.content)
        self.assertEquals(content.get('total'), 0)
        self.assertEquals(content.get('result'), [])


class UserAuthenticationHandlerTest(TestCase):

    def test_recover_password_success(self):
        factories.UserFactory.create(
            id=1,
            username="usertest",
            email='usertest@sodexoapp.com')

        ret = self.client.put('/access/userauthentication/1')

        self.assertEquals(ret.status_code, 200,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        content = json.loads(ret.content)
        self.assertEquals(content.get('result'), 'Sua nova senha foi gerada '\
            'com sucesso e enviada por email')

    def test_recover_password_not_found(self):

        ret = self.client.put('/access/userauthentication/1')

        self.assertEquals(ret.status_code, 404,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        self.assertEquals(ret.content, 'Not found')


class ChangeUserPasswordTeste(TestCase):

    def test_changed_success(self):
        user = factories.UserFactory.create(
            id=1,
            username="usertest",
            email='usertest@sodexoapp.com')
        oldpass = user.password
        cup = ChangeUserPassword()
        newPass = cup.aplyChange(user)
        self.assertNotEquals(oldpass, newPass)
        newUser = User.objects.get(id=user.id)
        self.assertNotEquals(oldpass, newUser.password)


class SendMailTest(TestCase):

    def test_email_params(self):
        send_generic_mail('Este é o assunto', 'Esta é a menssagem',
         ['tiagohl@outlook.com', '123@exemplo.com'])

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Este é o assunto')
        self.assertEqual(mail.outbox[0].body, 'Esta é a menssagem')
        self.assertEquals(mail.outbox[0].to[0], 'tiagohl@outlook.com')
        self.assertEquals(mail.outbox[0].to[1], '123@exemplo.com')

    def test_raise_value_error(self):
        self.assertRaises(ValueError, send_generic_mail, 'Este é o assunto',
                                'Esta é a menssagem', ['tiagoh@inatel.br', ''])
