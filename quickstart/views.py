from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from quickstart.MyApp import MessageClass, KeyboardClass, Data1Class
from rest_framework.parsers import JSONParser

from .models import mecabnouns

from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MessageView(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', None)
        get_arg2 = request.GET.get('arg2', None)

        # Any URL parameters get passed in **kw
        myClass = MessageClass(get_arg1, get_arg2, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kw):
        get_arg1 = request.POST.get("arg1",None)
        get_arg2 = request.data

        get_arg1 = get_arg2.get('content')
        print("return:{}".format(get_arg1))
        
        myClass = MessageClass(answer, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response

class KeyboardView(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', None)
        get_arg2 = request.GET.get('arg2', None)

        # Any URL parameters get passed in **kw
        myClass = KeyboardClass(get_arg1, get_arg2, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response


#data: 시각화
class Data1View(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.POST.get("arg1",None)
        get_arg2 = request.POST.get("arg2",None)
        # Any URL parameters get passed in **kw
        myClass = Data1Class(get_arg1, get_arg2, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response


    def post(self, request, *args, **kw):
        myClass = Data1Class("", "", *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response