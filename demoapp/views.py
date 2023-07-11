from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from .models import TeamMembers

# Create your views here.
def demo(request):
    obj1 = Place.objects.all()
    obj = TeamMembers.objects.all()
    return render(request, "index.html", {'result':obj,'result1':obj1})


#def addition(request):
 #   x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
 #   res1=x*y
 #   res2=x-y
  #  res3=x/y
  #  return render(request, "menu.html",{'result':(res,res1,res2,res3)})
# def demo1(request):
# return HttpResponse("Good Evening")
# def Detail(request):
# return render(request,"menu.html")
# def demo2(request):
# return HttpResponse("All is well")
