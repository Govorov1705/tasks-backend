from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from .models import Task
from .serializers import TaskSerializer
from .pagination import TaskPageNumberPagination


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPageNumberPagination

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('is_done', '-date_updated')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

class TaskRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk, owner=request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        task = get_object_or_404(Task, id=pk, owner=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        task = get_object_or_404(Task, id=pk, owner=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
