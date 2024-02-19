from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

from authsystem.models import User
from authsystem.serializers import UserPatchingSerializer

from tasks.models import MainTask, SubTask
from tasks.serilizers import (
    GetOnlyMainTaskSerilizer, GetOnlySubTaskSerilizer,

    MainTaskSerilizer, SubTaskSerilizer
    )
from projects.models import Project
from projects.serializers import GetOnlyProjectSerilizer, ProjectSerilizer

from services.queries import get_queryset_in_tasks



def _special_appending(request, queryset, query):
    try:
        parametr = request.query_params[query]
        return queryset.filter(Q(status_id=(int(parametr)+1))) if parametr == '0' or parametr == '1' else queryset
    except:
        return queryset
    
def _processing_return(request, serializers, projects, tasks, sub_tasks):
        try:
            parametr = request.query_params['low']

            return Response({
                'projects': serializers[parametr](projects, many=True).data,
                'tasks': serializers[parametr](tasks, many=True).data,
                'sub_tasks': serializers[parametr](sub_tasks, many=True).data,
            })
        except:
           return Response({
                'projects': serializers['0'](projects, many=True).data,
                'tasks': serializers['0'](tasks, many=True).data,
                'sub_tasks': serializers['0'](sub_tasks, many=True).data,
            })
        
class CheckUserStaticstickAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPatchingSerializer

    def get(self, request, *args, **kwargs):        
        #/api/v1/docs/utils/statists/7a987881-7933-4139-8092-e92ae6f60485/?end_tasks=0&end_tasks=0&end_subtasks=1&low=0&end_proj=1
        user = User.objects.get(id=self.kwargs['pk'])

        return _processing_return(request, 
                           {
                            '0': GetOnlySubTaskSerilizer,
                            '1': ProjectSerilizer,
                           }, 
                           _special_appending(self.request, Project.objects.filter(participants=user,), 'end_proj'), 
                           _special_appending(request, MainTask.objects.filter(participants=user), 'end_tasks'), 
                           _special_appending(self.request, SubTask.objects.filter(participants=user), 'end_subtasks'),
                           )