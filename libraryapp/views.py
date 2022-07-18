from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Customer, Loan
from .serializers import BookSerializer, CustomerSerializer, LoanSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.http.response import JsonResponse


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LoanView(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'age']
    search_fields = ['^first_name', 'last_name', 'city']
    ordering_fields = ['id', 'first_name', 'email']
