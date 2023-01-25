from django.shortcuts import render

# Create your views here.
def bookpage(request):
    return render(request,"myapp/bookpage.html")