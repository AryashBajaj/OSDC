from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login, logout
from forum.models import CustomUser, Question, Answer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer

class CreateUserView(generics.ListCreateAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetail(APIView) :
    permission_classes = [IsAuthenticated]

    def get_object(self, uid) :
        try :
            return CustomUser.objects.get(id = uid)
        except CustomUser.DoesNotExist :
            return None

    def get(self, request, uid) :
        user = self.get_object(uid)
        if user is not None :
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class Upvote(APIView) :
    permission_classes = [IsAuthenticated]

    def get_answer(self, aid) :
        try :
            return Answer.objects.get(id = aid)
        except Answer.DoesNotExist :
            return None
        
    def get_user(sef, uid) :
        try :
            return CustomUser.objects.get(id = uid)
        except CustomUser.DoesNotExist :
            return None
    
    def post(self, request, aid, uid) :
        user = self.get_user(uid)
        answer = self.get_user(aid)
        if user is not None and answer is not None :
            user.credit += 1
            answer.upvoted = True
            user.save()
            answer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)


class QuestionList(APIView) :
    permission_classes = [AllowAny]

    def get(self, request) :
        questions = Question.objects.all().order_by("-upvoted").order_by("-created_at")
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        query = request.data.get('query')
        if query is None :
            query = ""
        questions = Question.objects.filter(title__contains=query).order_by("-upvoted").order_by("-created_at")
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionCreateView(APIView) :
    permission_classes = [IsAuthenticated]

    def post(self, request) :
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionDetailView(APIView) :
    permission_classes = [IsAuthenticated]

    def get_object(self, qid):
        try:
            return Question.objects.get(id=qid)
        except Question.DoesNotExist:
            return None

    def get(self, request, qid):
        question = self.get_object(qid)
        if not question:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, qid):
        question = self.get_object(qid)
        if not question:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, qid):
        question = self.get_object(qid)
        if not question:
            return Response(status=status.HTTP_404_NOT_FOUND)
        question.delete()
        return Response(status=status.HTTP_200_OK)
    

class AnswerList(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request, qid) :
        question = None
        try :
            question = Question.objects.get(id = qid)
        except Question.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
        answers = Answer.objects.filter(answer_to = question)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, qid) :
        question = None
        try :
            question = Question.objects.get(id = qid)
        except Question.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(author = request.user, answer_to = question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnswerDetailView(APIView) :
    permission_classes = [IsAuthenticated]
        
    def get_answer(self, aid) :
        try :
            return Answer.objects.get(id = aid)
        except Answer.DoesNotExist :
            return None
        

    def get(self, request, aid) :
        answer = self.get_answer(aid)
        if answer is None :
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, aid) :
        answer = self.get_answer(aid)
        if answer is None :
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, aid) :
        answer = self.get_answer(aid)
        if answer is None :
            return Response(status=status.HTTP_404_NOT_FOUND)
        answer.delete()
        return Response(status=status.HTTP_200_OK)
    