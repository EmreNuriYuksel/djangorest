from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory

from .models import Customer


class CustomerTests(TestCase):

    def setUp(self):
        Customer.objects.create(customer_name="testName", customer_email="test@email.com")

    def test_customer_dbrecord(self):
        customer = Customer.objects.get(customer_name="testName")
        expected_object_name = f'{customer.customer_name}'
        self.assertEquals(expected_object_name, 'testName')

    def test_get_customer(self):
        url = "http://127.0.0.1/api/customer/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testName')

    def test_create_customer(self):
        response = self.client.post('/api/customer/', {'customer_name': 'tester',
                                                       'customer_email': 'tester@customer.com'})
        self.assertEqual(response.status_code, 201)

    def test_delete_customer(self):
        self.client.post('/api/customer/', {'customer_name': 'tester',
                                            'customer_email': 'tester@customer.com'})
        response = self.client.delete('/api/customer/2/')
        self.assertEqual(response.status_code, 204)

    def test_update_customer(self):
        response = self.client.put('/api/customer/1/', {'customer_name': 'updatedCustomer',
                                                        'customer_email': 'updated@customer.com'},
                                   content_type='application/json')
        self.assertContains(response, 'updatedCustomer')
        self.assertEqual(response.status_code, 200)
