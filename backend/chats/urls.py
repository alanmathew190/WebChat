from django.urls import path
from .views import CreateChat, UserChats, SendMessage, GetMessages

urlpatterns = [
    path('create/', CreateChat.as_view()),
    path('my-chats/', UserChats.as_view()),
    path('send/', SendMessage.as_view()),
    path('<int:chat_id>/messages/', GetMessages.as_view()),
]