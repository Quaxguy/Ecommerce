from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

#Custom User Manager 

class UserManager(BaseUserManager):
    def create_user(self, email, first_name,last_name,phone_number,email_token, password=None,password2=None):
        # """
        # Creates and saves a User with the given email, name ,tc , and password1
        if not email:
            raise ValueError("Users must have an email address")
        if not phone_number:
            raise ValueError("Users must have a phone number")
        user = self.model(
            email=self.normalize_email(email), 
            # normalising email 
            first_name=first_name,
            last_name=last_name, 
            email_token=email_token,
            phone_number=phone_number
        )

        user.set_password(password)
        #Password get hashed and saved 
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name,last_name,phone_number,password=None):
        # """
        # Creates and saves a superuser with the given email, date of
        # birth and password.
        # """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    first_name  = models.CharField(max_length=200,blank=False,null=True)
    last_name = models.CharField(max_length=200,blank=False,null=True)
    phone_number = models.CharField(max_length = 10,blank=False,null=True)
    is_email_verified = models.BooleanField(default=False)
    email_token=models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # Any user that is regestering is not a admin so is_admin=false

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","phone_number"]
    #email is required but it is used in  USERNAME_FIELD

    def __str__(self):
        return self.email
    # Whenever user object is shown so it is done with the help of email 
    # Ex : email1 object gives the data of user 1 

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin