from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from auth.manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

AUTH_PROVIDERS={'email':'email','google':'google'}

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True,verbose_name=_("Email Address"))
    first_name=models.CharField(max_length=100,verbose_name=_("First Name"))
    last_name=models.CharField(max_length=100,verbose_name=_("Last Name"))
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    date_joined=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    last_login=models.DateTimeField(auto_now=True)
    auth_provider=models.CharField(max_length=50,null=False,default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["first_name","last_name"]  

    objects=UserManager()    #for custom user model not superuser     

    def tokens(self):
         refresh = RefreshToken.for_user(self)
         return {
           'refresh':str(refresh),
           'access':str(refresh.access_token),
         }


    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name.title()}{self.last_name.title()}"
    

    
class OneTimeToken(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email_token=models.CharField(max_length=200)


    def __str__(self):
       return f"{self.user.first_name} - token"
