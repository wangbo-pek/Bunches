from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bunch01 import models


def test(request):
    person = models.Person.objects.all().values('id', 'name', 'age', 'gender')
    person_list = list(person)

    return JsonResponse({'data': person_list}, safe=True)
