from django.http import HttpResponse
from django.template import Template



def index(request):
    if request.method =="POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username,password)

    #return HttpResponse('HELLO WORLD!')
    return render(request,'index.html')
