from rest_framework import serializers
from .models import Chat, Message
from accounts.models import User

class ChatSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = Chat
        fields = ['id', 'participants', 'created_at']
    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'image', 'is_seen', 'created_at']
        read_only_fields = ['sender']