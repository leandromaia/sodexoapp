# encoding: utf-8
import json

from django.test import TestCase
from django.db.models.fields import *
from django.test.client import Client

from consultation.models import SodexoClient
from consultation import factories
from consultation import views
from django.contrib.auth import get_user_model
User = get_user_model()


class SodexoClientTetsCase(TestCase):
    def test_fields(self):
        meta = SodexoClient._meta

        self.assertIsInstance(meta.get_field('user'), related.ForeignKey)
        self.assertIsInstance(meta.get_field('name'), CharField)
        self.assertIsInstance(meta.get_field('cpf'), CharField)
        self.assertIsInstance(meta.get_field('card_number'), CharField)
        self.assertIsInstance(meta.get_field('daily_value'), DecimalField)

    def test_unicode(self):
        c = SodexoClient(name='name_test')
        self.assertEquals(str(c), c.name)


class SodexoClientHandlerTest(TestCase):
    fixture = ['basic_auth.yaml']

    def test_get_sodexo_client_url(self):
        c = Client()
        c.login(username='admin', password='admin')

        ret = c.get('/consultation/sodexoclient')
        self.assertEquals(ret.status_code, 200, 'wrong status code.')

    def test_get_list(self):

        user = factories.UserFactory.create(
            id=1,
            username="usertest",
            email='usertest@sodexoapp.com')

        factories.SodexoClientFactory.create(
            user=user,
            name='user',
            cpf='12345678912',
            card_number='123456789',
            daily_value=30)

        ret = self.client.get('/consultation/sodexoclient')

        self.assertEquals(ret.status_code, 200,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        content = json.loads(ret.content)
        self.assertEquals(content.get('total'), 1)

        sodexoclient = content.get('result')[0]
        self.assertEquals(sodexoclient.get('user').get('username'), 'usertest')
        self.assertEquals(sodexoclient.get('user').get('email'),
                          'usertest@sodexoapp.com')
        self.assertEquals(sodexoclient.get('name'), 'user')
        self.assertEquals(sodexoclient.get('cpf'), '12345678912')
        self.assertEquals(sodexoclient.get('card_number'), '123456789')
        self.assertEquals(sodexoclient.get('daily_value'), '30')

    def test_get_list_empty(self):
        ret = self.client.get('/consultation/sodexoclient')

        self.assertEquals(ret.status_code, 200,
                          'Status_code incorreto(%d)\n'
                          'Content: \n%s' % (ret.status_code, ret.content))

        content = json.loads(ret.content)
        self.assertEquals(content.get('total'), 0)
        self.assertEquals(content.get('result'), [])

    def test_post(self):
        data = {
            'name': 'leandro',
            'cpf': '25694845525',
            'card_number': '12169564',
            'daily_value': 15.0,
            'user': {
                'username': 'tiago',
                'email': 'tiago@inatel.br',
                'password': 'grs6955'
                }
        }

        c = Client()
        c.login(username='admin', password='admin')

        ret = c.post('/consultation/sodexoclient', json.dumps(data),\
                                            content_type='application/json')
        self.assertEquals(ret.status_code, 200,
            'Status_code incorreto(%d)\n'
            'Content: \n%s' % (ret.status_code, ret.content))

        id = json.loads(ret.content)['result']['id']

        sodexo_client = SodexoClient.objects.get(pk=id)
        self.assertEquals(sodexo_client.name, data['name'])
        self.assertEquals(sodexo_client.cpf, data['cpf'])
        self.assertEquals(sodexo_client.card_number, data['card_number'])
        self.assertEquals(sodexo_client.daily_value, data['daily_value'])
        self.assertEquals(sodexo_client.user.username, \
            data['user']['username'])
        self.assertEquals(sodexo_client.user.email, data['user']['email'])

    def test_post_sodexo_client_not_unique_cpf(self):
        user = factories.UserFactory.create(
            id=1,
            username="usertest",
            email='usertest@sodexoapp.com')

        factories.SodexoClientFactory.create(
            user=user,
            name='user',
            cpf='12345678912',
            card_number='123456789',
            daily_value=30.00)

        data = {
            'name': 'leandro',
            'cpf': '12345678912',
            'card_number': '12169564',
            'daily_value': 15.0,
            'user': {
                'username': 'leandro',
                'email': 'leandro@icc.br',
                'password': 'grs6955'
                }
        }

        c = Client()
        c.login(username='admin', password='admin')

        ret = c.post('/consultation/sodexoclient', json.dumps(data),\
                                            content_type='application/json')
        self.assertEquals(ret.status_code, 500,
            'Status_code incorreto(%d)\n'
            'Content: \n%s' % (ret.status_code, ret.content))


class PerformCalculationViewsTest(TestCase):

    def test_balance_greater_than_daily_value(self):
        user = factories.UserFactory.create()
        sodexo_client = factories.SodexoClientFactory.create(
            user=user,
            daily_value=18.0)
        result = views.perform_calculation(sodexo_client, 300)

        self.assertEquals(result['remaining_days'], '16')
        self.assertEquals(result['leftover'], '12.0')

    def test_balance_minor_than_daily_value(self):
        user = factories.UserFactory.create()
        sodexo_client = factories.SodexoClientFactory.create(
            user=user,
            daily_value=18.0)
        result = views.perform_calculation(sodexo_client, 10.0)

        self.assertEquals(result['remaining_days'], '0')
        self.assertEquals(result['leftover'], '10.0')

    def test_without_leftover(self):
        user = factories.UserFactory.create()
        sodexo_client = factories.SodexoClientFactory.create(
            user=user,
            daily_value=18.0)
        result = views.perform_calculation(sodexo_client, 90.0)

        self.assertEquals(result['remaining_days'], '5')
        self.assertEquals(result['leftover'], '0.0')

    def test_balance_decimal(self):
        user = factories.UserFactory.create()
        sodexo_client = factories.SodexoClientFactory.create(
            user=user,
            daily_value=18.0)
        result = views.perform_calculation(sodexo_client, 0.47)

        self.assertEquals(result['remaining_days'], '0')
        self.assertEquals(result['leftover'], '0.47')

    def test_balance_same_daily_value(self):
        user = factories.UserFactory.create()
        sodexo_client = factories.SodexoClientFactory.create(
            user=user,
            daily_value=18.0)
        result = views.perform_calculation(sodexo_client, 18.0)

        self.assertEquals(result['remaining_days'], '1')
        self.assertEquals(result['leftover'], '0.0')
