# from django.http import JsonResponse
from resume.models import Resume
from resume.permissions import IsOwnerOrReadOnly
from resume.serializers import ResumeSerializer
from rest_framework import viewsets, permissions


class ResumeView(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch']
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

