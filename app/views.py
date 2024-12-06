from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'name':'pujitha','age':121,'score':87}
    return render(request,'condition.html',context=d)