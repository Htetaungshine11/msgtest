from channels.generic.websocket import WebsocketConsumer
from frontend.models import group
from controls.models import Cuser
from rest_framework.serializers import ModelSerializer
from asgiref.sync import async_to_sync
import json
class sgr(ModelSerializer):
    class Meta:
        model = Cuser
        fields =['username',]

class web(WebsocketConsumer):
  

    def connect(self):
       
        self.accept()
        self.channel_group_name=self.scope['url_route']['kwargs']['name']
        self.u1=self.scope['user']
        a=group.objects.filter(groupname=self.channel_group_name)
        
        if not a:
            group.objects.create(groupname=self.channel_group_name)

        group.objects.filter(groupname=self.channel_group_name)[0].user.add(self.u1)
        b=group.objects.filter(groupname=self.channel_group_name)[0].user.all()
        self.send(text_data="anum\\"+str(len(group.objects.get(groupname=self.channel_group_name).user.all())-1)+'//'+json.dumps(sgr(b,many=True).data))
        
        async_to_sync(self.channel_layer.group_add)(self.channel_group_name,self.channel_name)
       
          
    
       

    def receive(self,text_data):
        
        async_to_sync(self.channel_layer.group_send)(self.channel_group_name,{
            "type":"sendfun",
            "data":text_data,
            
        })  

    def sendfun(self,event):
        self.send(text_data=event['data'])


    def disconnect(self,close_code):
        group.objects.filter(groupname=self.channel_group_name)[0].user.remove(self.u1)
        async_to_sync(self.channel_layer.group_discard)(self.channel_group_name,self.channel_name)