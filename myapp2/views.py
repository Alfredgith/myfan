from django.shortcuts import render,redirect
from .models import who,pic
from .forms import mywho,mypic
from django.http import HttpResponse


def run(request):
    if request.method=='POST':
       form=mywho(request.POST)
       if form.is_valid():
          form.save()
    else:
       form=mywho() 
       new=who.objects.all() 
       return render(request,'index.html2',{'form':form,'new':new})     

def ran(request):
    if request.method=='POST':
       form1=mypic(request.POST,request.FILES)
       if form1.is_valid():
          form1.save()
          return redirect('/ran')
    else:
        form1=mypic() 
        new1=pic.objects.all() 
        return render(request,'index.html3',{'form1':form1,'new1':new1})
    

def box(request):
    return render(request,'index.html4')