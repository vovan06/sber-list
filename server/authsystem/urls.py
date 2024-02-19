from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView, ChangePasswordView)

from .views import (
    LoginAPIView, RegisterAPIView,UserInformationAndPatchingRetrieveAPIView,
    UserInformationAndPatchingListView, PasswordRestoreAPIView, StartingPasswordRestoreAPIView
)

urlpatterns = [
    # TO-DO: перед продом вырезать к хуям
    path('users/', UserInformationAndPatchingListView.as_view()),

    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/changes/', UserInformationAndPatchingRetrieveAPIView.as_view(), name='user_progile_changing'),

    path('password/restore/start/', StartingPasswordRestoreAPIView.as_view()),
    path('password/restore/', PasswordRestoreAPIView.as_view()),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
