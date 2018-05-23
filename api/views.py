# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import *
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def elem_list(request):        
    if request.method == 'GET':
        elements = Abrahammr.objects.all()
        serializer = AbrahammrSerializer(elements, many=True)        
        print 'se manda lista'
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AbrahammrSerializer(data=request.data)
        if serializer.is_valid():
            elem = serializer.save()                        
            print 'se guardo elemento '
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def elem_get(request, pk):
    
    try:
        elem = Abrahammr.objects.get(pk=pk)
        print 'elemento obtenido'
    except Abrahammr.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AbrahammrSerializer(elem)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AbrahammrSerializer(elem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        elem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
