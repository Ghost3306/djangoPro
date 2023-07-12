from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from polls import CrMLData 
from .CrMLData import *
from django.utils import timezone

# Create your views here.
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print("Entered Message is : ",message)
        res = response(message)
        return JsonResponse({'message': message, 'response': res})
    return render(request, 'chatbot.html')



    