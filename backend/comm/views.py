from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login, logout
from forum.models import CustomUser
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status, generics
from rest_framework.views import APIView

# Create your views here.
