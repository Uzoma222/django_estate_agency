from django.shortcuts import render, redirect,get_object_or_404
from.models import Mymessages
from django.contrib import messages
from datetime import datetime
from.models import Users



def message(request):
    fname= request.POST['fullname']
    email= request.POST['email']
    phone= request.POST['phone']
    msg= request.POST['msg']
    pname= request.POST['pname']
    plocation= request.POST['plocation']
    agentid= request.POST['agentid']
    pid= request.POST['pid']

    agent = get_object_or_404(Users,pk=agentid)


    contact= Mymessages(agent_id=agent, name=fname,email=email, phone=phone, comment=msg, pname=pname,plocation=plocation,msg_date=datetime.now)

    contact.save()
    messages.success(request, 'your request has been submitted,Agent will contact you soon')
    return redirect('/listing/single/'+ pid)
    