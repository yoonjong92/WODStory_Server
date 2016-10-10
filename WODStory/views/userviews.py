from django.contrib.auth.models import User
from WODStory.models import WOD
from WODStory.views.wodviews import WODSerializer
from rest_framework import serializers, generics

class UserSerializer(serializers.HyperlinkedModelSerializer):
    wods = WODSerializer(many=True, read_only=True)
    #serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
    class Meta:
        model = User
        fields = ('id', 'username', 'wods')

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
