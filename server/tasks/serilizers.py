from rest_framework import serializers

from .models import MainTask, SubTask, TaskStatus
from authsystem.models import User
from authsystem.serializers import UserPatchingSerializer

class TaskStatusSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'



class SubTaskSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

class GetOnlySubTaskSerilizer(serializers.ModelSerializer):
    participants = UserPatchingSerializer(many=True,)
    class Meta:
        model = SubTask
        fields = '__all__'



class MainTaskSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MainTask
        fields = '__all__'

    def validate(self, data):
        return data

class GetOnlyMainTaskSerilizer(serializers.ModelSerializer):
    sub_task = SubTaskSerilizer(many=True,)
    participants = UserPatchingSerializer(many=True,)

    class Meta:
        model = MainTask
        fields = '__all__'

    def validate(self, data):
        return data
