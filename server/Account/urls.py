from django.urls import path
from .views import UserRegistrationView,EmailVerificationView,UserLoginView


urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('verify-email/<str:email_token>/',EmailVerificationView.as_view(),name='verify-email'),
    path('login/',UserLoginView.as_view(),name='login')
]