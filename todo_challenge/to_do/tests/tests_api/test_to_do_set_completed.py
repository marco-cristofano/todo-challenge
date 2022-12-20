from rest_framework.test import APITestCase
from to_do.models import ToDo


class SetCompletedToDoTest(APITestCase):
    url = '/api/to_do/'

    def setUp(self):
        self.to_do = ToDo.objects.create(
            title='titulo',
            description='descripcion',
            completed=False
        )

    def _get_url(self, id):
        return self.url + str(id) + '/completed/'

    def test_update_ok(self):
        url = self._get_url(self.to_do.id)
        response = self.client.put(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        to_do = response.data
        self.assertEqual(to_do['title'], 'titulo')
        self.assertEqual(to_do['description'], 'descripcion')
        self.assertTrue(to_do['completed'])
        self.assertContains(response, 'created', 1, status_code=200)
        self.assertContains(response, 'last_modification', 1, status_code=200)
