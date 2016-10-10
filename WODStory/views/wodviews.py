from django.contrib.auth.models import User
from WODStory.models import WOD, Workout, WorkoutType, WODType
from rest_framework import serializers, generics
from rest_framework import permissions
from WODStory.permissions import IsAuthorOrReadOnly

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('name','weight','distance','reps',)


class WODSerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(many=True)

    def create(self, validiated_data):
        author = User(id=validiated_data['author'])
        wodtype = WODType(id=validiated_data['type'])
        wod = WOD.objects.create(author = validiated_data['author'],title = validiated_data['title'],type = validiated_data['type'],
        text = validiated_data['text'],result_reps = validiated_data['result_reps'])
        if 'result_time' in validiated_data:
            wod.result_time = validiated_data['result_time']
        if 'result_rounds' in validiated_data:
            wod.result_rounds = validiated_data['result_rounds']
        for item in validiated_data['workouts']:
            workouttype, created = WorkoutType.objects.get_or_create(name = item['name'])
            workout = Workout.objects.create(name = workouttype, reps = item['reps'], wod = wod)
            if 'weight' in item:
                workout.weight = item['weight']
            if 'distance' in item:
                workout.distance = item['distance']
            workout.save()
        return wod

    class Meta:
        model = WOD
        fields = ('id', 'author', 'title', 'text', 'type', 'workouts', 'result_time', 'result_rounds', 'result_reps')

class WODSList(generics.ListCreateAPIView):
    queryset = WOD.objects.all()
    serializer_class = WODSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class WODDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WOD.objects.all()
    serializer_class = WODSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)


#필요없는 것
class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
