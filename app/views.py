from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Carousel
from app.serializers import CarouselSerializer


def api(request):
    return JsonResponse({'code': 200})


