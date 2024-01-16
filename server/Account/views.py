from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Account.serializers import UserRegistrationSerializers,UserLoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
#from account.renderers import UserRenderer
from Account.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from Account.utils import send_email_verification_mail
# from rest_framework.permissions import IsAuthenticated


#TOKEN GENERATION MANUALLLY#
def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }

class UserRegistrationView(APIView):
   # renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializers=UserRegistrationSerializers(data=request.data)
        if serializers.is_valid():
             user = serializers.save()
             try:
                # print(user.username)
                print(user.email_token)
                # Save the serializer data directly
                # token=get_tokens_for_user(user) #token for logging and register NOT FOR EMAIL!!!!!
                # print(token)
                send_email_verification_mail(user, user.email_token)
             except:
                 return Response(
                     {'detail': 'Error sending email verification mail.'},
                      status=status.HTTP_500_INTERNAL_SERVER_ERROR
                 )
            #user=serializers.save()
             return Response({'msg':'Registration successfull'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

class EmailVerificationView(APIView):
    def get(self, request, email_token):
        user = get_object_or_404(User, email_token=email_token)
        
        if user.is_email_verified:
            return Response({'detail': 'Email is already verified.'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_email_verified = True
        user.is_active = True
        user.save()

        return Response({'detail': 'Email verified successfully.'}, status=status.HTTP_200_OK)
    
class UserLoginView(APIView):
#   renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    print(email)
    password = serializer.data.get('password')
    print(password)
    user = authenticate(email=email, password=password)
    
    print(user)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

 