from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from app.models import Book
from app.serializers import BookSerializer
from goods.models import Goods


def api(request):
    return JsonResponse({'code': 200})


class BookView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    # book_queryset = Book.objects.all()
    def get(self, request):
        book_queryset = Book.objects.all()
        ser_obj = BookSerializer(book_queryset, many=True)
        return Response(ser_obj.data)

    def post(self, request):
        book_obj = request.data
        print(book_obj)
        ser_obj = BookSerializer(data=book_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.validated_data)

        return Response(ser_obj.errors)
