from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.core.paginator import Paginator 

class Sim(APIView):
    # get request
    def get_available(self, request):

        # object that stores my data
        available = Stock.objects.all()
        paginator = Paginator(available, 1) # query paginator

        page_no = request.GET.get('page')
        page_obj = paginator.get_page(page_no)

        goods = StockSerializers(available, many=True)
        return Response(goods.data, {'page_obj': page_obj})

    # post request
    def set_limit(self):
        pass

