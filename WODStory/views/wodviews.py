from django.contrib.auth import get_user_model
from WODStory.models import WOD, Workout, WorkoutType, WODType
from rest_framework import serializers, generics
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from WODStory.permissions import IsAuthorOrReadOnly

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout

class WorkoutTypeSerializer(serializers.ModelSerializer):

    def to_representation(self,obj):
        return obj.name
    class Meta:
        model = WorkoutType


class WODSerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(many=True)
    date = serializers.DateField(format="%Y-%m-%d",input_formats="%Y-%m-%d",)
    def to_internal_value(self, data):
        return data

    def create(self, validiated_data):
        user = self.context['request'].user
        wodtype = WODType(id=validiated_data['type'])
        wod = WOD.objects.create(user = user,title = validiated_data['title'],type = wodtype,
        text = validiated_data['text'],date = validiated_data['date'])
        if 'round' in validiated_data:
            wod.round = validiated_data['round']
        if 'emomminute' in validiated_data:
            wod.emomminute = validiated_data['emomminute']
        if 'emomperminute' in validiated_data:
            wod.emomperminute = validiated_data['emomperminute']
        if 'result_time' in validiated_data:
            wod.result_time = validiated_data['result_time']
        if 'result_rounds' in validiated_data:
            wod.result_rounds = validiated_data['result_rounds']
        if 'result_reps' in validiated_data:
            wod.result_reps = validiated_data['result_reps']
        for item in validiated_data['workouts']:
            workouttype, created = WorkoutType.objects.get_or_create(name = item['name'])
            if created:
                workouttype.count = 1
            else:
                workouttype.count = workouttype.count + 1
            workouttype.save()
            workout = Workout.objects.create(name = workouttype, wod = wod, user = user, date = validiated_data['date'])
            if 'weight' in item:
                workout.weight = item['weight']
            if 'weight_unit' in item:
                workout.weight_unit = item['weight_unit']
            if 'content' in item:
                workout.content = item['content']
            workout.save()
        wod.save()
        return wod

    class Meta:
        model = WOD
        fields = ('id', 'user', 'title', 'text', 'type', 'date', 'round', 'emomminute', 'emomperminute', 'workouts', 'result_time', 'result_rounds', 'result_reps')

class WODSearchSerializer(serializers.ModelSerializer):
    wod = WODSerializer()
#    def to_representation(self,obj):
#        return obj.wod

    class Meta:
        model = Workout
        fields = ('wod', 'user', 'name')

class WODSList(generics.ListCreateAPIView):
#    queryset = WOD.objects.all()
    serializer_class = WODSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-date',)
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)

    def get_queryset(self):
#        user = self.request.user
#        return WOD.objects.filter(user=user)
        qset = WOD.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            qset = qset.filter(user_id=user_id)
        return qset

class WODSearch(generics.ListAPIView):
    serializer_class = WODSearchSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-date',)

    def get_queryset(self):
        qset = Workout.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            qset = qset.filter(user_id=user_id)
        type_name = self.request.query_params.get('name', None)
        if type_name is not None:
            qset = qset.filter(name = type_name)
        return qset


class WODDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WOD.objects.all()
    serializer_class = WODSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)


class WorkoutTypeList(generics.ListCreateAPIView):
    queryset = WorkoutType.objects.all()
    serializer_class = WorkoutTypeSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-count',)

#필요없는 것
class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
