from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login, logout
from forum.models import CustomUser
from comm.models import Server, Channel, Message
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from comm.serializers import ServerSerializer, ChannelSerializer, MessageSerializer

# Create your views here.

class ServerList(APIView) :

    permission_classes = [IsAuthenticated]

    def get(self, request) :
        servers = request.user.server_set.all()
        serializer = ServerSerializer(servers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ServerSearchView(APIView) :
    permission_classes = [AllowAny]            

    def get(self, request) :
        servers = Server.object.all()
        serializer = ServerSerializer(servers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ServerDetailView(APIView) :
    permission_classes = [IsAuthenticated]

    def get_object(self, sid) :
        try :
            return Server.objects.get(id = sid)
        except Server.DoesNotExist :
            return None
        
    def get(self, request, sid) :
        server = self.get_object(sid)
        if server is not None :
            serializer = ServerSerializer(server)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request, sid) :
        server = self.get_object(sid)
        if server is not None :
            serializer = ServerSerializer(server, request.data, partial = True)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

       
class ChannelList(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request, sid) :
        channels = Channel.objects.filter(inServer = sid)
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, sid) :
        server = None
        try :
            server = Server.objects.get(id = 1)
        except Server.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(inServer = server)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChanneLDetailView(APIView) :
    permission_classes = [IsAuthenticated]

    def get_object(self, cid) :
        try :
            return Channel.objects.get(id = cid)
        except :
            return None
        
    def get(self, request, cid) :
        channel = self.get_object(cid)
        if channel is not None :
            serializer = ChannelSerializer(channel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, cid) :
        channel = self.get_object(cid)
        if channel is not None :
            serializer = ChannelSerializer(channel, data=request.data, partial=True)
            if serializer.is_valid() :
                serializer.save()                                                                               
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, cid) :
        channel = self.get_object(cid)
        if channel is not None :
            channel.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class MessageList(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request, cid) :
        messages = Message.objects.filter(inChannel=cid)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, cid) :
        channel = None
        try :
            channel = Channel.objects.get(id = cid)
        except Channel.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save(author=request.user, inChannel = channel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MessageDetail(APIView) :
    permission_classes = [IsAuthenticated]

    def get_object(self, mid) :
        try :
            return Message.objects.get(id = mid)
        except Message.DoesNotExist :
            return None
    
    def put(self, request, mid) :
        message = self.get_object(mid)
        if message is not None :
            serializer = MessageSerializer(message, data=request.data, partial=True)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status==status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, mid) :
        message = self.get_object(mid)
        if message is not None :
            message.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status==status.HTTP_404_NOT_FOUND)
    

    

    
