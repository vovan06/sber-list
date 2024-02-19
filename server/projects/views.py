from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    ListAPIView, RetrieveAPIView, GenericAPIView)
from tasks.models import TaskStatus

from .models import Project
from authsystem.models import User
from .serializers import (
    ProjectSerilizer, GetOnlyProjectSerilizer,
    InviteLinkSerializer,)
from services.queries import get_queryset_in_tasks
from services.http_requests import (
    _destroy, _post, 
    _put, _update,
)
from services.task import  _archive_project, sending_mail
from server.settings import ALLOWED_HOSTS

class SendInviteLinkAPIView(GenericAPIView):
    serializer_class = InviteLinkSerializer

    def post(self, request, *args, **kwargs):
        # try:
            email=request.POST['email']
            project=request.POST['project_id']
            sending_mail(
                email, 
                'Invite link',
                f'http://{ALLOWED_HOSTS[0]}/api/v1/docs/projects/invite/link/confirmation/?email={email}&project={project}',)
            return Response({'detail': 'message has been sended'},)
        # except:
        #     return Response({'detail': 'error. check email'},)

class ConfirmationLinkAPIView(GenericAPIView):
    serializer_class = InviteLinkSerializer

    def post(self, request, *args, **kwargs):
        try:
            email = request.query_params['email']
            project_id = request.query_params['project_id']
            user = User.objects.get(email=email)
            project = Project.objects.get(id=project_id)
            project.participants.add(user) 
            print(project.participants)
            project.save()
            return Response(GetOnlyProjectSerilizer(project).data)
        except:
            return Response({'detail': 'error. check email'},)

class ProjectAPIView(ListCreateAPIView):
    queryset = Project.objects.prefetch_related()
    serializer_class = ProjectSerilizer
    _my_detail_serializer = GetOnlyProjectSerilizer
    _my_model = Project

    def get_queryset(self, *args):
        return get_queryset_in_tasks(self.request, self.queryset, self._my_model)

    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)

    def post(self, request, *args, **kwargs):
        return _post(request, self.get_serializer, self.perform_create, self._my_model, self._my_detail_serializer)

class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerilizer
    _my_detail_serializer = GetOnlyProjectSerilizer
    _my_model = Project

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
    

class ProjectsForUserAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerilizer
    _my_detail_serializer = GetOnlyProjectSerilizer
    _my_model = Project

    def get_queryset(self):
        return get_queryset_in_tasks(self.request, self.queryset, self._my_model).filter(participants=User.objects.get(id=self.kwargs['pk']))

    def get(self, request, *args, **kwargs):
        return Response(self._my_detail_serializer(self.get_queryset(), many=True).data)
    

class ArchiveProject(RetrieveAPIView):    
    queryset = Project.objects.all()
    serializer_class = ProjectSerilizer
    _my_detail_serializer = GetOnlyProjectSerilizer
    _my_model = Project

    def get_queryset(self):
        req = self._my_model.objects.filter(id=self.kwargs['pk'])
        if len(req) == 0:
            raise Http404
        else:
            return req

    def get(self, request, *args, **kwargs):
        return Response(GetOnlyProjectSerilizer(self.get_queryset(), many=True).data)
    
    def post(self, request, *args, **kwargs):
        _archive_project(
            project=self.get_queryset()[0],
            instance=TaskStatus.objects.get(pk=1),
            )
        return Response({'detail': 'successful started'}, status=status.HTTP_202_ACCEPTED)