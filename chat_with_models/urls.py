from django.urls import path
from . import views 

urlpatterns = [
    path("chat-with-groq/", views.chat_with_groq, name='Testing groq')
]


