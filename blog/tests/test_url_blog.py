from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views
class TestPostUrl(SimpleTestCase):
    def test_url_blog_post_list_resolve(self):
        url = reverse('blog:list')
        return self.assertEquals(resolve(url).func.view_class, views.PostListView)
    
    def test_url_blog_post_detail_resolve(self):
        url = reverse('blog:detail', kwargs={'pk':21})
        return self.assertEquals(resolve(url).func.view_class, views.PostDetailView)
    
    def test_url_blog_post_create_resolve(self):
        url = reverse('blog:create')
        return self.assertEquals(resolve(url).func.view_class, views.PostCreateView)
    
    def test_url_blog_post_update_resolve(self):
        url = reverse('blog:update', kwargs={'pk':21})
        return self.assertEquals(resolve(url).func.view_class, views.PostUpdateView)
    
    def test_url_blog_post_delete_resolve(self):
        url = reverse('blog:delete', kwargs={'pk':21})
        return self.assertEquals(resolve(url).func.view_class, views.PostDeleteView)