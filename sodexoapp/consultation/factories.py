from consultation.models import SodexoClient
from django.contrib.auth import get_user_model
User = get_user_model()

import factory


class SodexoClientFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SodexoClient
    user = factory.Sequence(lambda x: 'sodexo_user%d' % x)
    name = factory.Sequence(lambda x: '%duser' % x)
    cpf = factory.Sequence(lambda x: '1215781584%d' % x)
    card_number = factory.Sequence(lambda x: '%d23456789' % x)
    daily_value = factory.Sequence(lambda x: '%f' % x)


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda x: 'sodexo_user%d' % x)
    email = factory.Sequence(lambda x: '%duser@sodexoapp.com' % x)
    password = 'abc'
