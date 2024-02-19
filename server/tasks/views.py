from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from authsystem.models import User
from services.queries import get_queryset_in_tasks
from .models import TaskStatus, MainTask, SubTask
from .serilizers import (
    TaskStatusSerilizer, 
    MainTaskSerilizer, GetOnlyMainTaskSerilizer, 
    SubTaskSerilizer, GetOnlySubTaskSerilizer,)
from services.http_requests import (
    _destroy, _post, 
    _put, _update,
)

class MainTaskForUserAPIView(ListAPIView):
    queryset = MainTask.objects.all()
    serializer_class = MainTaskSerilizer
    _my_detail_serializer = GetOnlyMainTaskSerilizer
    _my_model = MainTask

    def get_queryset(self):
        return get_queryset_in_tasks(self.request, self.queryset, self._my_model).filter(participants=User.objects.get(id=self.kwargs['pk']))

    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)

class SubTaskForUserAPIView(ListAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerilizer
    _my_detail_serializer = GetOnlySubTaskSerilizer
    _my_model = SubTask

    def get_queryset(self):
        return get_queryset_in_tasks(self.request, self.queryset, self._my_model).filter(participants=User.objects.get(id=self.kwargs['pk']))

    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)
    


class TaskStatusAPIView(ListCreateAPIView):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerilizer

class TaskStatusDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerilizer


class MainTaskAPIView(ListCreateAPIView):
    queryset = MainTask.objects.prefetch_related()
    serializer_class = MainTaskSerilizer
    _my_detail_serializer = GetOnlyMainTaskSerilizer
    _my_model = MainTask

    def get_queryset(self, *args):
        return get_queryset_in_tasks(self.request, self.queryset, self._my_model)
    
    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)

    def post(self, request, *args, **kwargs):
        return _post(request, self.get_serializer, self.perform_create, self._my_model, self._my_detail_serializer)

class MainTaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MainTask.objects.all()
    serializer_class = MainTaskSerilizer
    _my_detail_serializer = GetOnlyMainTaskSerilizer
    _my_model = MainTask
    
    def get_queryset(self):
        req = self._my_model.objects.filter(id=self.kwargs['pk'])
        if len(req) == 0:
            raise Http404
        else:
            return req

    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)

    def put(self, request, *args, **kwargs):
        return _put(request, self.get_serializer, self.get_object, self.perform_update, self._my_model, self._my_detail_serializer,)
    
    def patch(self, request, *args, **kwargs):
        return _update(request, self.get_object, self.get_serializer, self.perform_update, self._my_model, self._my_detail_serializer, *args, **kwargs) 
    
    def delete(self, request, *args, **kwargs):
        return _destroy(request, self.get_object, self.perform_destroy, *args, **kwargs)


class SubTaskAPIView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerilizer
    _my_detail_serializer = GetOnlySubTaskSerilizer
    _my_model = SubTask

    def get_queryset(self, *args):
        return get_queryset_in_tasks(self.request, self.queryset, self._my_model)
    
    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)

    def post(self, request, *args, **kwargs):
        return _post(request, self.get_serializer, self.perform_create, self._my_model, self._my_detail_serializer)

class SubTaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerilizer
    _my_detail_serializer = GetOnlySubTaskSerilizer
    _my_model = SubTask

    def get_queryset(self):
        req = self._my_model.objects.filter(id=self.kwargs['pk'])
        print(req)
        if len(req) == 0:
            raise Http404
        else:
            return req

    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)

    def put(self, request, *args, **kwargs):
        return _put(request, self.get_serializer, self.get_object, self.perform_update, self._my_model, self._my_detail_serializer,)
    
    def patch(self, request, *args, **kwargs):
        return _update(request, self.get_object, self.get_serializer, self.perform_update, self._my_model, self._my_detail_serializer, *args, **kwargs) 
    
    def delete(self, request, *args, **kwargs):
        return _destroy(request, self.get_object, self.perform_destroy, *args, **kwargs)