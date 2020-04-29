from django.test import TestCase
from .models import DefaultPost


class DefaultPostTest(TestCase):
    test_post_text = 'Тестовый пост'

    def test_create_post(self):
        new_post = DefaultPost(title=self.test_post_text, description='Тестовое описание')
        new_post.save()
        assert DefaultPost.objects.first().title == self.test_post_text
