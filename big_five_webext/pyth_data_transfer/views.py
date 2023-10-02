# Create your views here.
import numpy as np
# In your Django app's views.py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import semantic_search

score_arr_full = semantic_search.score_arr_full
@api_view(['GET'])
def my_api_endpoint(request):
    # Handle the request and prepare a response
    response_data = {"message": score_arr_full}
    return Response(response_data)

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
# Create your views here.
