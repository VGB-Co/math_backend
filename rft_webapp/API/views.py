# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response
import jwt
from datetime import datetime, timedelta

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20


# Create your views here.
@api_view(['GET'])
def taskreq(request):
    encoded_user = jwt.encode({'user_id': "abcd"}, 'SECRET', algorithm='HS256')
    return Response(encoded_user)

def encode(h, p):
    header = base64UrlEncode(JSON.stringify(h));
    payload = base64UrlEncode(JSON.stringify(p));
    return header + '.' + payload