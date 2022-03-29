from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def firstApi (request):
    message = 'Congratulations, you have created an API'
    return Response(message)
