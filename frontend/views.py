from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View

@login_required(login_url="login")
def home(request):
    a=render(request,'base.html',{})
    a['Cache-Control'] = f'max-age={60*60*24}'
    return a

class Chatroom(View):
    def get(self, request,name):
        return render(request,'room.html',{})

    

