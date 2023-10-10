from django.test import TestCase, Client
from .models import Todo
import json

# Create your tests here.

data = [
    {
    'id': 1,
    'title': 'test 001',
    'complete': False
    },
    {
    'id': 2,
    'title': 'test 002',
    'complete': True
    },
]

class ToDoListTestCase(TestCase):
    def setUp(self) -> None:
        # 新增資料
        todo1 = Todo(title=data[0]['title'], complete=data[0]['complete'])
        todo1.save()
        todo2 = Todo(title=data[1]['title'], complete=data[1]['complete'])
        todo2.save()
        
        # 建立client
        self.client = Client()


    def test_index(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed("index.html")


    # def test_get_all_data(self):
    #     res = self.client.get("/api/")
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(json.loads(res.content)['data'][0]['title'], data[0]['title'])
        