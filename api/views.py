from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

class Numbers(generics.ListCreateAPIView):
    def post(self, request):
        print(type(request.data['numbers']))
        try:
            li = list(map(int, request.data['numbers'][1:-1].split(",")))
        except:
            return Response({"is_success": False,"user_id": "amber_sanghvi_14112000"})
        print(type(li[0]))
        print((li[0]))
        even = []
        odd = []
        flag = False
        for i in li:
            try:
                if isinstance(i,int):
                    if int(i)%2==0:
                        even.append(int(i))
                    else:
                        odd.append(int(i))
                else:
                    flag = True
            except:
                flag = True
        print(odd,even)
        if not flag:
            response = {"is_success": True,"user_id": "amber_sanghvi_14112000",  "odd": odd, "even": even}
        else:
            response = {"is_success": False,"user_id": "amber_sanghvi_14112000"}
        return Response(response)