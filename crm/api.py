from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from .serializers import *


class Customers(APIView):

    def get(self, request):
        model = Customer.objects.all()
        serializer = CustomerSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):

    def get(self, request, customer_id):
        if not self.find_customer(customer_id):
            return Response(f'Customer with id: {customer_id} could not be found.', status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(self.find_customer(customer_id))
        return Response(serializer.data)

    def put(self, request, customer_id):
        if not self.find_customer(customer_id):
            return Response(f'Customer with id: {customer_id} could not be found.', status=status.HTTP_404_NOT_FOUND)
        model = self.find_customer(customer_id)
        serializer = CustomerSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id):
        if not self.find_customer(customer_id):
            return Response(f'Customer with id: {customer_id} could not be found.', status=status.HTTP_404_NOT_FOUND)
        model = self.find_customer(customer_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def find_customer(customer_id):
        try:
            model = Customer.objects.get(id=customer_id)
            return model
        except Customer.DoesNotExist:
            return
