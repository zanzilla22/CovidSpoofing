from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime

def index(request):
    return render(request, "covidCocaine/index.html", {
        "dateAndTheTime": f"Valid {datetime.date.today().strftime('%B')} {datetime.date.today().day}, {datetime.date.today().year}",
        "theTime": f"from {datetime.datetime.now().time().strftime('%#I:%M')} {datetime.datetime.now().time().strftime('%p')[0].lower()}.m. to 11:59 {datetime.datetime.now().time().strftime('%p')[0].lower()}.m.",
    })

def otherIteration(request):
    return render(request, "covidCocaine/otherIteration.html")