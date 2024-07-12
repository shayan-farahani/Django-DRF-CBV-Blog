from django.test import TestCase

from ..models import Post, Category, Comment

class TestPostModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='test'
        )
        self.post = Post.objects.create(
            title='test',
            body='test',
        )
        self.comment = Comment.objects.create(
            author='test',
            body='test',
            post=self.post,
        )

    def test_create_post_with_valid_data(self):
        self.assertTrue(Post.objects.filter(pk = self.post.id).exists())

    def test_create_comment_with_valid_data(self):
        self.assertTrue(Comment.objects.filter(pk = self.comment.id).exists())
        
    def test_create_category_with_valid_data(self):
        self.assertTrue(Category.objects.filter(pk = self.category.id).exists())

    


