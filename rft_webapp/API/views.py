from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rft_webapp.queries import query
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from django.http import JsonResponse
from rest_framework.response import Response
from rft_webapp.API.serializers import TaskSerializer, TopListSerializer
from rft_webapp.mathematic.models import Task
from rft_webapp.database.models import Results
from rft_webapp.mathematic import generator
from rft_webapp.mathematic import enums

# Constants variables.
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username", "")
    password = request.data.get("password", "")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'name': user.username, 'email': user.email},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    username = request.data.get("username", "")
    password = request.data.get("password", "")
    email = request.data.get("email", "")
    
    if username is None or password is None or email is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, email=email, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'name': user.username, 'email': user.email},
                    status=HTTP_200_OK)



@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def taskList(request):
    difficulty = request.GET.get('difficulty', None)
    if not difficulty is None:
        difficulty = int(difficulty)
        print(difficulty)
        if difficulty == 0:
            generator.Generator.generatings(50, enums.Type.EASY)
        elif difficulty == 1:
            generator.Generator.generatings(50, enums.Type.INTERMEDIATE)
        elif difficulty == 2:
            generator.Generator.generatings(50, enums.Type.ADVANCED)

        tasks = Task.objects.all().order_by('-id')[:10]

        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, status=HTTP_200_OK, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def result(request):
    correct_answer = request.data.get("correct_answer", 0)
    time = request.data.get("time", 0)
    difficulty = request.GET.get("difficulty", 0)
    user = request.user
    if float(time) > 0:
        query.insertresults(user, difficulty, time, correct_answer)
        return Response("OK", status=HTTP_200_OK)
    else:
        return Response("error: wrong time", status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def toplists(request):
    difficulty = request.GET.get("difficulty", "")
    difficulty = int(difficulty)
    top = Results.objects.all().filter(type=difficulty).order_by('time')[:10]
    serializer = TopListSerializer(top, many=True)
    return JsonResponse({"users": serializer.data}, safe=False, status=HTTP_200_OK)