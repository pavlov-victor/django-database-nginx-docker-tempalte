from django.test import TestCase
from .models import DefaultPost

class DefaultPostTest(TestCase):

    def test_create_post(self):
        new_post = DefaultPost(title='Тестовый пост', description='Тестовое описание')
        new_post.save()
        taked_new_post = DefaultPost.objects.first()
        assert taked_new_post.title == 'Тестовый пост'
