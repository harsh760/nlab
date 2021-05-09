from django.urls import path, include , re_path
from .views import register , usersignin , getAdvisor , addAdvisor , bookAdvisor ,getCalls

urlpatterns = [
    # path('ordercount/<pk>/',ordercount,name="ordercount"),
    path('user/register', register , name="register"),
    path('user/login', usersignin  , name="login"),
    path('user/<int:userid>/advisor' , getAdvisor , name="getadvisor"),
    path('admin/advisor',addAdvisor , name="addadvisor"),
    path('user/<int:user_id>/advisor/<int:advisor_id>',bookAdvisor, name="bookAdvisor"),
    path('user/<int:user_id>/advisor/booking/',getCalls)
    # path('del/<pk>', deleteBB , name="del"),

]