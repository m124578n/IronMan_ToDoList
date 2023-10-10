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
        Todo.objects.create(title=data[0]['title'], complete=data[0]['complete'])
        Todo.objects.create(title=data[1]['title'], complete=data[1]['complete'])
        
        # 建立client
        self.client = Client()


    def test_index(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed("index.html")


    def test_get_all_todos(self):
        res = self.client.get("/api/")
        res_datas = json.loads(res.content)['data']
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_datas[0]['title'], data[0]['title'])


    def test_add_new_todo(self):
        test_data = {'title': 'test 003'}
        res = self.client.post(
                "/api/add/", 
                json.dumps(test_data), 
                content_type="application/json"
            )
        res_data = json.loads(res.content)
        self.assertEqual(res_data['todo_title'], test_data['title'])
        self.assertEqual(res_data['complete'], False)
    
    