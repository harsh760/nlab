from django.shortcuts import render , get_object_or_404
from django.views.decorators.csrf import  csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializer import RegistrationSerializer , UserSigninSerializer , AdvisorSerializer ,AddAdvisorSerializer , BookAdvisorSerializer , CallsSerializer
from .models import User , Advisor , Calls
# Create your views here.

@api_view(['POST',])
@permission_classes([AllowAny])
def register(request, *args, **kwargs):
    serializer = RegistrationSerializer(data=request.data, many=False)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        user.save()
        data['status_code'] = 200
        data['details'] = "Successfully registered a new user"
        return Response(data=data, status=status.HTTP_201_CREATED)
    else:
        data['status_code'] = 400
        data['details'] = serializer.errors
        return Response(data=data)

@api_view(["POST",])
@permission_classes([AllowAny])
def usersignin(request):
    signin_serializer = UserSigninSerializer(data=request.data)
    data = {}
   
    if signin_serializer.is_valid():
        user = signin_serializer.save()
        # token, _ = Token.objects.get_or_create(user=user)
        # is_expired, token = token_expire_handler(token)
        
        data['status_code'] = 200
        # data['details'] = 'Token is issued'
        print(user)
        #details
        data['user_id'] = user.id
        # data['token'] = token.key
        # data['expires_in'] = expires_in(token)
        # data['first_name']=user.first_name
        # data['last_name']=user.last_name
        # data['city']=user.city
        # data['area']=user.area

        # consumer=Consumer.objects.get(user_id=user.id)
        # data['ref_code']=consumer.ref_code

        return Response(data=data, status=status.HTTP_201_CREATED)
    else:
        data['status_code'] = 404
        data['details'] =signin_serializer.errors
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    # return Response("hello world")

@api_view(["GET",])
@permission_classes([AllowAny])
def getAdvisor(request , **kwargs):
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
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def getCalls(request , user_id):
    ad = Calls.objects.filter(user = user_id)
    print(ad)
    data = {}
    serializer = CallsSerializer(ad , many=True)
    return Response(data=serializer.data , status=status.HTTP_200_OK)
