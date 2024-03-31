from django.contrib.auth import get_user_model
from django.db.models import Count, Subquery
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *


class ReportItemsViewSet(viewsets.ModelViewSet):
    queryset = ReportItem.objects.all()
    serializer_class = ReportItemSerializer

    def create(self, request, *args, **kwargs):
        url = kwargs.get('resourceUrl')
        blockedResourcesQuery = BlockedResource.objects.filter(url=url)
        if not len(blockedResourcesQuery):
            resource = BlockedResource.objects.create(url=url)
            resource.save()
        else:
            resource = blockedResourcesQuery[0]
        return ReportItem.objects.create(resource=resource)

class BlockedResourcesViewSet(viewsets.ModelViewSet):
    serializer_class = BlockedResourceSerializer

    def get_queryset(self):
        qs = BlockedResource.objects.annotate(calls_number=Count('reportitem')).all()
        return qs
