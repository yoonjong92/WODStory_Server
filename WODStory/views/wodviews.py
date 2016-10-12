from django.contrib.auth import get_user_model
from WODStory.models import WOD, Workout, WorkoutType, WODType
from rest_framework import serializers, generics
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from WODStory.permissions import IsAuthorOrReadOnly

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('name','weight','distance','reps',)


class WODSerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(many=True)

    def create(self, validiated_data):
        user = get_user_model()(id=validiated_data['user'])
        wodtype = WODType(id=validiated_data['type'])
        wod = WOD.objects.create(user = self.request.user.id,title = validiated_data['title'],type = validiated_data['type'],
        text = validiated_data['text'],result_reps = validiated_data['result_reps'])
        if 'result_time' in validiated_data:
            wod.result_time = validiated_data['result_time']
        if 'result_rounds' in validiated_data:
            wod.result_rounds = validiated_data['result_rounds']
        for item in validiated_data['workouts']:
            workouttype, created = WorkoutType.objects.get_or_create(name = item['name'])
            workout = Workout.objects.create(name = workouttype, wod = wod)
            if 'weight' in item:
                workout.weight = item['weight']
            if 'distance' in item:
                workout.distance = item['distance']
            if 'reps' in item:
                workout.reps = item['reps']
            workout.save()
        wod.save()
        return wod

    class Meta:
        model = WOD
        fields = ('id', 'user', 'title', 'text', 'type', 'workouts', 'result_time', 'result_rounds', 'result_reps')

class WODSList(generics.ListCreateAPIView):
#    queryset = WOD.objects.all()
    serializer_class = WODSerializer
    pagination_class = LimitOffsetPagination
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)

    def get_queryset(self):
#        user = self.request.user
#        return WOD.objects.filter(user=user)
        qset = WOD.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            qset = qset.filter(user_id=user_id)
        return qset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WODDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WOD.objects.all()
    serializer_class = WODSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)


#필요없는 것
class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
