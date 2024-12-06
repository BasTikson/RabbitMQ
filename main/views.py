from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AboutUs, RequestLog
from .serializers import AboutUsSerializer, RequestLogSerializer


class AboutView(TemplateView):
    template_name = "main/about.html"


class AboutViewSomeUrl(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/about_some_url.html'

    def get(self, request):
        about_us = AboutUs.objects.first()
        serializer = AboutUsSerializer(about_us)
        return Response({'about_us': serializer.data})


class RequestLogView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/request_logs.html'

    def get(self, request):
        logs = RequestLog.objects.all().order_by('-timestamp')
        serializer = RequestLogSerializer(logs, many=True)
        return Response({'logs': serializer.data})
