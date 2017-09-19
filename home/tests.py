from django.test import TestCase

from .models import User


class TestUser(TestCase):
    """Test User model, check that all attributes are set as expected."""
    def setUp(self):
        self.user = User.objects.create_user(
            username='username',
            email='username@mail.ru',
            first_name='Sergey',
            last_name='Lobanov'
        )

    def test_user_get_by_attributes(self):
        self.assertEqual(User.objects.get(username='username'), self.user)
        self.assertEqual(User.objects.get(email='username@mail.ru'), self.user)
        self.assertEqual(User.objects.get(id=1), self.user)

    def test_user_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'Sergey Lobanov')

    def test_user_get_short_name_email(self):
        self.user.first_name = ''
        self.user.last_name = ''

        self.assertEqual(self.user.get_short_name(), 'username@mail.ru')
