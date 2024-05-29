from rest_framework import serializers
from forum.models import CustomUser, Question, Answer

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = CustomUser
        fields = ["id", "username", "password"]
        extra_kwargs = {"password" : {"write_only" : True}}

        def create(self, validated_data) :
            print(validated_data)
            user = CustomUser.objects.create_user(**validated_data)
            return user

class QuestionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question
        fields = ["id", "title", "content", "created_at", "author", "img", "upvoted"]
        extra_kwargs = {"author" : {"read_only" : True}}

class AnswerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Answer
        fields = ["id", "content", "created_at", "author", "answer_to", "upvoted"]
        extra_kwargs = {"author" : {"read_only" : True}, "answer_to" : {"read_only" : True}}


    