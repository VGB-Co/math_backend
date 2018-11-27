from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from django.http import JsonResponse
from rest_framework.response import Response
from rft_webapp.API.serializers import TaskSerializer
from rft_webapp.mathematic.models import Task

# Constants variables.
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

@api_view(["GET"])
def taskList(request):
    difficulty = request.data.get("difficulty")
<<<<<<< HEAD
    tasks = Task.objects.all()
=======
    tasks
>>>>>>> 4c69584028852cf21e3ec05d1d3afa832090d8eb
    if difficulty == 0:
        pass
    elif difficulty == 1:
        pass
    elif difficulty == 2:
        pass
    
<<<<<<< HEAD
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, status=HTTP_200_OK, safe=False)
=======
     return Response(tasks, status=HTTP_200_OK)
>>>>>>> 4c69584028852cf21e3ec05d1d3afa832090d8eb
