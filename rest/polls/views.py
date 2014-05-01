#!/usr/bin/python
from django.shortcuts import render
from django.http import HttpResponse
from search import phone


def index(request):
    phone_app = phone.Search()
    params = request.GET
    phone_nr = str(params['phone'])

    if phone_nr.isdigit():
        data = phone_app.get(phone_nr)

        if data is False:
            data = ''

        return HttpResponse(data)
    else:
        return HttpResponse("Phone nr must be digits.")
