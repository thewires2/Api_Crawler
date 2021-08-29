from django.shortcuts import render
from .models import Category, SubCategory
from .service import getapilist, getcategory, createnewtoken
import datetime, time

bearer = createnewtoken()
curr = datetime.datetime.now().strftime(f"%H:%M")


def home(request):
    if Category.objects.count() == 0:
        getcategory()
    return render(request, 'crawler/home.html', {
        "Categories": Category.objects.all(),
    })


def getsubcategories(request):
    if SubCategory.objects.count() <= 400:
        getapilist()
    return render(request, 'crawler/categories.html', {
        "data": SubCategory.objects.all()
    })
