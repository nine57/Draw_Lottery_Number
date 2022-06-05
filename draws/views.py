from django.http import HttpResponse
import requests
import random

from django.shortcuts import render
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from draws.serializers import NumberSerializer
from draws.models import Number, Count


class NumberView(APIView):
    def get_weight(self):
        counts = Count.objects.all()[:]
        weight = [1]*45

        for count in counts:
            idx = count.id-1
            cnt = count.cnt
            weight[idx] = cnt
        return weight

    @swagger_auto_schema(operation_description="Get Random Number")
    def get(self, request):
        WEIGHT = self.get_weight()

        dmnd = request.GET.getlist('dmnd', None)
        dmnd = list(map(int, dmnd))

        number_pool = list(range(1, 46))
        wins = [] + dmnd
        count = 0 + len(dmnd)
        while count < 6:
            draw = random.choices(number_pool, weights=WEIGHT)[0]
            if draw in wins:
                continue
            wins.append(draw)
            count += 1

        wins.sort()
        return render(request, "draws.html", {"wins": wins}, status=200)
        # return Response({"result": wins}, status=200)


class CountView(APIView):
    DRAWN_NUMBER_API = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='

    @transaction.atomic()
    def get(self, request):
        last_update = Number.objects.last()
        num = last_update.drwNo+1

        while True:
            URL = self.DRAWN_NUMBER_API+str(num)
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
    #     URL = self.DRAWN_NUMBER_API+'1'
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

