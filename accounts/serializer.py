from .models import User , Advisor , Calls
from rest_framework import serializers
from django.contrib.auth import authenticate
import datetime
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class RegistrationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        data={}
        old = User.objects.filter(email__iexact=self.validated_data['email'])
        if not old.exists():
            old = old.first()
            user=User(
                name=self.validated_data['name'],
                email=self.validated_data['email'],
            )
            password=self.validated_data['password']
            user.set_password(password)
            user.save()
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
            return user , jwt_token
        else:
            data['status_code']=400
            data['details']='User already exist'
            raise serializers.ValidationError(data)

class UserSigninSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=35)
    class Meta:
        model=User
        # fields = ("__all__")
        fields=('email','password')
        
    def save(self):
        username = self.validated_data['email']
        password = self.validated_data['password']
        
        user = authenticate(
                username = username,
                password = password 
            )
        if user is None:
            raise serializers.ValidationError()
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError()
        return {
            'user_id':user.id,
            'jwt_token': jwt_token
        }

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('__all__')

class AddAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('name','photo_url')
    def addadvisor(self):
        name= self.validated_data['name']
        url = self.validated_data['photo_url']
        ad = Advisor(name = name , photo_url=url)
        ad.save()
        return ad

class BookAdvisorSerializer(serializers.Serializer):
    # class Meta:
        # model = Calls
        # fields = ()
    datetime = serializers.DateTimeField()
    def save(self):
        uid = self.context.get('uid')
        aid = self.context.get('aid')

        advisor=Advisor.objects.get(id=aid)
        user=User.objects.get(id=uid)
        datetime = self.validated_data['datetime']
        # print("in again")
        # dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")

        book = Calls(advisor = advisor , user = user , datetime=datetime)
        book.save()
        return book

class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls
        fields = ("id" ,"datetime" , "advisor")
        depth = 1
