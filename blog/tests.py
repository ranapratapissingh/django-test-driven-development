from django.test import TestCase
from .models import Entry, Comment
from django.contrib.auth import get_user_model

# Create your tests here.

class EntryModelTest(TestCase):

    def test_string_representation(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)


    def test_verbose_name_plural(self):
    	self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")


    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')
        self.entry = Entry.objects.create(title='1-title', body='1-body',
                                          author=self.user)

    def test_one_entry(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_two_entries(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        Entry.objects.create(title='2-title', body='2-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')

    def test_basic_view(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_get_absolute_url(self):
	    user = get_user_model().objects.get(username='some_user')
	    entry = Entry.objects.create(title="My entry title", author=user)
	    self.assertIsNotNone(entry.get_absolute_url())

class EntryViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='demo_user')
        self.entry = Entry.objects.create(title='1-title', body='1-body', author=self.user)
    
    def test_title_in_entry(self):
        Entry.objects.create(title='1-title', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
    
    def test_body_in_entry(self):
        Entry.objects.create(body='1-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-body')

class CommentModelTest(TestCase):

    def test_string_representation(self):
        comment = Comment(body="My comment body")
        self.assertEqual(str(comment), "My comment body")