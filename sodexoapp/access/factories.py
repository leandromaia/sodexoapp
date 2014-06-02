from django.contrib.auth import get_user_model
User = get_user_model()

import factory


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda x: 'sodexo_user%d' % x)
    email = factory.Sequence(lambda x: '%duser@sodexoapp.com' % x)
    password = 'abc'

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
