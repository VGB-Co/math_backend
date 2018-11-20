# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response
#import jwt


# Create your views here.
@api_view(['GET'])
def taskreq(request):
    r = request.META.get('HTTP_AUTHENTICATION')
    return Response("Hello Világ")
