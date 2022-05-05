import requests
import random

from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from draws.serializers import NumberSerializer
from draws.models import Number, Count


# for dev #TODO
WEIGHT = [143, 136, 134, 139, 130, 126, 133, 131, 106, 139, 134, 142, 144, 142, 135, 131, 144, 147, 133, 140, 135, 114,
          121, 135, 129, 132, 145, 124, 123, 121, 135, 114, 140, 152, 125, 134, 140, 133, 145, 141, 123, 133, 146, 135, 140]
DRAWN_NUMBER_API = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
LAST_UPDATE = ''
UPDATED_NO = 1


class NumberView(APIView):
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


class CountView(APIView):
    @transaction.atomic()
    def get(self, request):
        last_update = Number.objects.last()
        num = last_update.drwNo+1

        while True:
            URL = DRAWN_NUMBER_API+str(num)
            req = requests.get(URL).json()
            return_checker = req.get("returnValue", None)
            if return_checker != 'success':
                break

            serializer = NumberSerializer(data=req)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors)

            if req.get('drwNo') == 100:
                break
            num += 1

        return Response({"result": f"Draw No {num} updated"})

    @transaction.atomic()
    def post(self, request):
        draws = Number.objects.all()
        for draw in draws:
            one = Count.objects.get(id=draw.drwtNo1)
            two = Count.objects.get(id=draw.drwtNo2)
            thr = Count.objects.get(id=draw.drwtNo3)
            fou = Count.objects.get(id=draw.drwtNo4)
            fiv = Count.objects.get(id=draw.drwtNo5)
            six = Count.objects.get(id=draw.drwtNo6)
            bns = Count.objects.get(id=draw.bnusNo)

            one.cnt += 1
            two.cnt += 1
            thr.cnt += 1
            fou.cnt += 1
            fiv.cnt += 1
            six.cnt += 1
            bns.bns += 1

            one.save()
            two.save()
            thr.save()
            fou.save()
            fiv.save()
            six.save()
            bns.save()

        return Response({"result": "Success"})

    # ------------------for setting up------------------

    # # for setting the first draw
    # def get(self, request):
    #     URL = DRAWN_NUMBER_API+'1'
    #     req = requests.get(URL).json()
    #     serializer = NumberSerializer(data=req)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"result": "Success"})
    #     return Response(serializer.errors)

    # # for setting the number 45
    # def post(self, request):
    #     for i in range(45):
    #         Count.objects.create(cnt=0)
    #     return Response({"result": "Success"})

    # # for clear count
    # def post(self, request):
    #     draws = Count.objects.all()
    #     for draw in draws:
    #         draw.cnt = 0
    #         draw.bns = 0
    #         draw.save()
    #     return Response({"result": "Success"})
