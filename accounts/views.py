from django.shortcuts import render , get_object_or_404
from django.views.decorators.csrf import  csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializer import RegistrationSerializer , UserSigninSerializer , AdvisorSerializer ,AddAdvisorSerializer , BookAdvisorSerializer , CallsSerializer
from .models import User , Advisor , Calls
# Create your views here.

@api_view(['POST',])
@permission_classes([AllowAny])
def register(request, *args, **kwargs):
    serializer = RegistrationSerializer(data=request.data, many=False)
    data = {}
    if serializer.is_valid():
        user , token = serializer.save()
        data['user_id'] = user.id
        data['jwt_token'] = token
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(["POST",])
@permission_classes([AllowAny])
def usersignin(request):
    signin_serializer = UserSigninSerializer(data=request.data)
    data = {}
   
    if signin_serializer.is_valid():
        user = signin_serializer.save()
        
        data['user_id'] = user['user_id']
        data['jwt_token'] = user['jwt_token']
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    # return Response("hello world")

@api_view(["GET",])
@permission_classes([IsAuthenticated])
def getAdvisor(request , **kwargs):
    # authentcation_class = JSONWebTokenAuthentication
    ad = Advisor.objects.all()
    serializer = AdvisorSerializer(ad , many=True)
    return Response(data = serializer.data , status=status.HTTP_200_OK)


@api_view(['POST',])
@permission_classes([AllowAny])
def addAdvisor(request):
    serializer = AddAdvisorSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.addadvisor()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def bookAdvisor(request,user_id,advisor_id):
    serializer = BookAdvisorSerializer(data=request.data, many=False , context={'uid': user_id , 'aid':advisor_id})
    if serializer.is_valid():
        print("in")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print("out")
        return Response(data = serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET",])
@permission_classes([IsAuthenticated])
def getCalls(request , user_id):
    ad = Calls.objects.filter(user = user_id)
    data = {}
    serializer = CallsSerializer(ad , many=True)
    return Response(data=serializer.data , status=status.HTTP_200_OK)
