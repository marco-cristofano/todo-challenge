from rest_framework.test import APITestCase
from to_do.models import ToDo


class ListToDoTest(APITestCase):
    url = '/api/to_do/'

    def setUp(self):
        self.to_do = ToDo.objects.create(
            title='titulo',
            description='descripcion',
            completed=False
        )
        self.to_do = ToDo.objects.create(
            title='titulo1',
            description='descripcion2',
            completed=True
        )

    def test_list_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        to_do = response.data[0]
        self.assertEqual(to_do['title'], 'titulo')
        self.assertEqual(to_do['description'], 'descripcion')
        self.assertEqual(to_do['completed'], False)
        to_do = response.data[1]
        self.assertEqual(to_do['title'], 'titulo1')
        self.assertEqual(to_do['description'], 'descripcion2')
        self.assertEqual(to_do['completed'], True)
        self.assertContains(response, 'created', 2, status_code=200)
        self.assertContains(response, 'last_modification', 2, status_code=200)
