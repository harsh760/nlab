from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self , password=None, name=None, email=None,is_staff=False,is_admin=False,is_active=True):
    
        user = self.model(
            name=name,
            email=email
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,password, name ,email =None ):
        user = self.create_user(
            password,
            name,
            email
        )
        user.staff = True
        user.admin = True   
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length = 25 , blank=False , null=False)
    email = models.EmailField(unique = True ,  max_length=35, blank=False, null=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = UserManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    
    @property
    def is_active(self):
        return self.active


class Advisor(models.Model):
	name = models.CharField(max_length=30, null=False)
	photo_url = models.CharField(max_length=200, null=False)

class Calls(models.Model):
	advisor = models.ForeignKey(Advisor, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	datetime = models.DateTimeField(null=False)