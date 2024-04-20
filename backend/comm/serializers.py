from comm.models import Server, Channel, Message
from rest_framework import serializers

class ServerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Server
        fields = ["id", "name", "img", "created_at"]

class ChannelSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Channel
        fields = ["id", "name", "inServer", "created_at"]
        extra_kwargs = {"inServer" : {"read_only" : True}}

class MessageSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Message
        fields = ["id", "content", "img", "author", "inChannel"]
        extra_kwargs = {"author" : {"read_only" : True}, "inChannel" : {"read_only" : True}}