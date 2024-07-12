from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post


class TestPostView(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title='test',
            body='test',
        )
    def test_blog_list_post_successful_response(self):
        url = reverse('blog:list')
        response = self.client.get(url)
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='blog/post_list.html')

    def test_blog_detail_post_successful_response(self):
        url = reverse('blog:detail', kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='blog/post_detail.html')
    

