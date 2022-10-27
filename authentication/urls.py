from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from authentication.views import RegisterView, ContactList, ContactDetailView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('token/', obtain_auth_token),
    path('contact/', ContactList.as_view()),
    path('contact/<int:id>/', ContactDetailView.as_view()),
]
