from rest_framework.test import APITestCase
from to_do.models import ToDo


class DeleteToDoTest(APITestCase):
    url = '/api/to_do/'

    def setUp(self):
        self.to_do = ToDo.objects.create(
            title='titulo',
            description='descripcion',
            completed=False
        )

    def _get_url(self, id):
        return self.url + str(id) + '/'

    def test_create_ok(self):
        url = self._get_url(self.to_do.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(ToDo.objects.count(), 0)
        self.assertEqual(ToDo.all_objects.count(), 1)
