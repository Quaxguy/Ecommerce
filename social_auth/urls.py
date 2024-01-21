from django.urls import path

from social_auth.views import GoogleSignInView

urlpatterns=[
    path('google/',GoogleSignInView.as_view(),name='google')
]