from django.urls import path

from .views import (
    ProjectAPIView, ProjectDetailAPIView, 
    ProjectsForUserAPIView, ArchiveProject,
    ConfirmationLinkAPIView, SendInviteLinkAPIView
    )

urlpatterns = [
    path('', ProjectAPIView.as_view(), name='project_list'),
    path('<uuid:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
    path('by/user/<uuid:pk>/', ProjectsForUserAPIView.as_view(), name='projects_list_by_user'),

    path('archive/<uuid:pk>/', ArchiveProject.as_view()),

    path('invite/link/', SendInviteLinkAPIView.as_view(), name='link_create'),
    path('invite/link/confirmation/', ConfirmationLinkAPIView.as_view(), name='link_confirmation'),
]
