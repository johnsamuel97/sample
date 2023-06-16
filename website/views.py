from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from website.forms import Sign_up
from django.http import HttpResponseRedirect
from website.models import Record
from website.forms import Insert_record


def Home_view(request):
    #record=Record.objects.all()
    return render(request, 'home.html',)

#def Login_view(request):
   #return render(request, 'login.html')

def Logout_view(request):
       return render(request, 'logout.html')

def Register_view(request):
   return render(request, 'register.html')
@login_required
def AboutUs_view(request):
    return render(request, 'aboutus.html')

@login_required
def Data_view(request):
    record=Record.objects.all()
    return render(request,'data.html',{'record':record})

def Signup_view(request):
    form=Sign_up()
    if request.method=="POST":
        form=Sign_up(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'signup.html',{"form":form})
def customer_record(request,id):
    customer_record=Record.objects.get(id=id)
    return render(request,'record.html',{'customer_record':customer_record})


def delete_record(request,id):
    delete_it=Record.objects.get(id=id)
    delete_it.delete()
    return redirect('/data')

def insert_view(request):
    form = Insert_record()
    if request.method=="POST":
        form=Insert_record(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request,'insert.html',{'form':form})
def update_record(request,id):
    current_record=Record.objects.get(id=id)
    form=Insert_record(request.POST or None, instance=current_record)
    if form.is_valid():
       form.save()
       return redirect('/')
    return render(request,'update.html',{'form':form})
def Tech(request):
    return render(request,'tech.html')