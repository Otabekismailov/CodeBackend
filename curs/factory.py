import datetime

import factory
import factory.django

from account import models


class RandomUserFactory(factory.Factory):
    class Meta:
        model = models.User.objects.all()

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
