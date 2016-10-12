from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from rest_framework import serializers, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from WODStory.models import WOD
from WODStory.views.wodviews import WODSerializer



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        instance.authtoken = token.key
        instance.save()

class UserSerializer(serializers.ModelSerializer):
    #serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
    def to_internal_value(self, data):
        return data
    def create(self, validiated_data):
        user, created = get_user_model().objects.get_or_create(username = validiated_data['username'])
        user.set_password(validiated_data['password'])
        if 'email' in validiated_data:
            user.email = validiated_data['email']
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'authtoken','password')

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class AuthwithToken(APIView):
    serializer_class = UserSerializer
    def get(self,request, format=None):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
