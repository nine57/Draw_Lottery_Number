import requests
import random

from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import NumberSerializer
from .models import Number


# for dev #TODO
WEIGHT = [143, 136, 134, 139, 130, 126, 133, 131, 106, 139, 134, 142, 144, 142, 135, 131, 144, 147, 133, 140, 135, 114,
          121, 135, 129, 132, 145, 124, 123, 121, 135, 114, 140, 152, 125, 134, 140, 133, 145, 141, 123, 133, 146, 135, 140]
DRAWN_NUMBER_API = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
LAST_UPDATE = ''
UPDATED_NO = 1


class DrawNumberView(APIView):
    @swagger_auto_schema(operation_description="Get Random Number")
    def get(self, request):
        except_numbers = request.GET.get('except', None)
        print(except_numbers, type(except_numbers))

        number_pool = list(range(1, 46))
        wins = []
        weight = WEIGHT[:]

        for _ in range(6):
            draw = random.choices(number_pool, weights=weight)
            idx = number_pool.index(draw[0])
            weight.pop(idx)
            wins.append(number_pool.pop(idx))

        return Response({"result": wins}, status=200)


class GetNumberView(APIView):
    @transaction.atomic()
    def post(self, request):

        URL = DRAWN_NUMBER_API+'1'
        req = requests.get(URL).json()

        print(req)

        serializer = NumberSerializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": "updated"})

        return Response(serializer.errors)
