from main.models import User
from main.tests.base.base import BaseViewsTest
from main.tests.base.decorators import active_users
from main.tests.base.taboo_methods import *


def serialize(obj, fields):
    return {key: getattr(obj, key) for key in fields}


class UsersViewTest(
    BaseViewsTest,
    TabooListMixin,
    TabooRetrieveMixin,
    TabooCreateMixin,
    TabooDeleteMixin
):
    def setUp(self):
        self.uri = 'users'
        self.model = User

    def get_self_response(self, user):
        return user.get(self.uri + 'self/')

    @active_users
    def test_self(self, user):
        response = self.get_self_response(user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = serialize(
            User.objects.get(id=user.id),
            ('id', 'username')
        )
        self.assertEqual(response.data, expected_data)


class Blocks(BaseViewsTest, TabooNoAuthDeleteMixin, TabooNoAuthCreateMixin, TabooNoAuthUpdateMixin):
    pass
