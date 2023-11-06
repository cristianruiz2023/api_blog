from django.test import TestCase
import pytest
# from ddf import G
from users.models import User
# from faker import Faker
#
# fake = Faker()
#
#
# @pytest.fixture
# def common_user_creation():
#     return G(User)
#
#
# @pytest.mark.django_db
# def test_common_user_creation(common_user_creation):
#     assert common_user_creation.username == 'cris'
#
#
# @pytest.mark.django_db
# def test_superuser_creation():
#     user = User.objects.create_superuser(
#         username='cris',
#         email='cris@admin.py',
#         password='12345678'
#
#     )
#     assert user.is_superuser
#
# @pytest.mark.django_db
# def test_staff_user_creation():
#     user = User.objects.create(
#         username='cris',
#         email='cris@admin.py',
#         password='12345678',
#         is_staff=True,
#
#     )
#     assert user.is_staff
#
# @pytest.mark.django_db
# def test_user_creation_fail():
#     with pytest.raises(Exception):
#         User.objects.create_user(
#             password='12345678',
#             is_staff=False,
#         )


class UserTestCase(TestCase):
    def setup(self):
        self.user = User.objects.create_user(
            password='12345678',
            is_staff=False,
        )
        
    def test_user_creation(self):
        assert self.user.is_active
        assert self.user.is_staff
        assert self.user.is_superuser
