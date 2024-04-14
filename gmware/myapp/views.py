from django.shortcuts import render
from .models import CUser
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.db.models import Avg
from django.db.models import Q


# Create your views here.

def function(request):
    # a=CUser.objects.all()
    # d=0
    # # b=0
    # # for i in a:
    # #     b+=i.score
    # #     d=b/len(a)
    # #     print(i.score)
    # b=map(lambda a:d+=i for i in a )
        
    mean_score = CUser.objects.aggregate(Avg('score'))
    avg_mean=CUser.objects.filter(score=CUser.objects.aggregate(Avg('score'))["score__avg"])
    # highest_score_user = CUser.objects.order_by('score').last()
    lessthan=CUser.objects.filter(score__lt=30).exists()
    # CUser.objects.update(score=100)
    # f=CUser.objects.filter(Q(score=20) | Q( score=10))
    # f=CUser.objects.exclude(score__in=(10,20))
    # f=CUser.objects.all()[2:]
    score_values_excluding_first_10 = CUser.objects.values_list('score', flat=True)[10:]
    print(list(score_values_excluding_first_10))

    return  HttpResponse(score_values_excluding_first_10)
    # return JsonResponse({"Msg":f.score})


    
    
