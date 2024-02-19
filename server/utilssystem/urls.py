from django.urls import path

from .views import CheckUserStaticstickAPIView

urlpatterns = [
    path('statists/<uuid:pk>/', CheckUserStaticstickAPIView.as_view(),),
]