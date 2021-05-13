from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Cuser
class uform(UserCreationForm):
    class Meta:
        model=Cuser
        fields=['email','username',]
def register(request):
    a=uform()
    if request.method == 'POST':
        a=uform(request.POST)
        if a.is_valid():
            a.save()
            return redirect('login')
        else:
            return render(request,"registration/register.html",{"form":a})
    return render(request,"registration/register.html",{"form":a})