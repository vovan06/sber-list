from rest_framework import serializers

from .models import Project
from authsystem.serializers import UserPatchingSerializer
from tasks.serilizers import MainTaskSerilizer


class InviteLinkSerializer(serializers.Serializer):
    project_id = serializers.UUIDField()
    email = serializers.EmailField()

class ProjectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class GetOnlyProjectSerilizer(serializers.ModelSerializer):
    participants = UserPatchingSerializer(many=True,)
    tasks = MainTaskSerilizer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
