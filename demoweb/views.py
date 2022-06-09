from datetime import datetime
import imp
from django.shortcuts import render,HttpResponse
from subprocess import run,PIPE
from datetime import datetime
import sys
from demoweb.models import Contact, VulScan
# Create your views here.
def index(request):
    return render(request , 'index.html')
def Vulnerabilityscanner(request):
    if request.method == "POST":
        site = request.POST.get('site')
        vulscan = VulScan(site=site, date = datetime.today())
        vulscan.save()
    #     inp = request.POST.get('site')
    #     out = run([sys.executable,"C://Users//patel//Desktop//WORK//FINAL YEAR PROJECT//Django//project1//vulnscan.py",inp],shell=False,stdout=PIPE)
    #     print(out)
    #     return render(request ,'external.html',{'data1':out.stdout})
    #     # return render(request, 'external.html')
    return render(request , 'Vulnerability.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today()) 
        contact.save()
        return render(request,'result.html')
    return render(request , 'contact.html')
def result(request):
    return render(request,'result.html')
def external(request):
    inp = request.POST.get('site')
    out = run([sys.executable,"C://Users//patel//Desktop//WORK//FINAL YEAR PROJECT//Django//project1//vulnscan.py",inp],shell=False,stdout=PIPE)
    print(out)
    return render(request ,'external.html',{'data1':out.stdout})

    