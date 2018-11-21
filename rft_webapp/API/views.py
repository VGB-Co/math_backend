# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


# Create your views here.
'''@api_view(['GET'])
def taskreq(request):
    encoded_user = jwt.encode({'user_id': "abcd"}, 'SECRET', algorithm='HS256')
    return Response(encoded_user)'''
@api_view(['GET'])
def sds(request):
    r = requests.get('https://api.github.com/events')
    return Response(r)