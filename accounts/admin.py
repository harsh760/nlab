from django.contrib import admin
from .models import User , Calls , Advisor

# Register your models here.

admin.site.register(User)
admin.site.register(Calls)
admin.site.register(Advisor)