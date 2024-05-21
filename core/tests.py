from django.test import TestCase, Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = models.Task.objects.create(
            title="Купить продукты",
            description="Сходить в магазин и купить молоко, яйца, хлеб, и овощи.",
            important=False,
            completed=False
        )

        self.test_task = {
            'title': 'Написать отчет',
            'description': 'Подготовить отчет по проекту.',
            'important': True,
            'completed': False
        }

    def test_detail_task(self):
        response = self.client.get(f'/task/{self.task.id}/')
        self.assertEquals(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/simple_redirect_view/')
        self.assertEquals(response.status_code, 302)

    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_important(self):
        response = self.client.get('/important/')
        self.assertEquals(response.status_code, 200)

    def test_simple_list_view(self):
        response = self.client.get('/simple_list_view/')
        self.assertEquals(response.status_code, 200)

    def test_completed(self):
        response = self.client.get('/completed/')
        self.assertEquals(response.status_code, 200)

    def test_simple_form_view_get(self):
        response = self.client.get('/simple_form_view/')
        self.assertEquals(response.status_code, 200)

    def test_simple_form_view_post(self):
        response = self.client.post('/simple_form_view/', data=self.test_task)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Task.objects.count(), 2)
        task = models.Task.objects.get(title=self.test_task['title'])
        self.assertEqual(task.description, self.test_task['description'])
        self.assertEqual(task.important, self.test_task['important'])
        self.assertEqual(task.completed, self.test_task['completed'])
