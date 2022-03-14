
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from cartapp.models import product


def searchresult(request):
    pro=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        pro=product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'pro':pro})
