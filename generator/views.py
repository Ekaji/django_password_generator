from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U"
,"V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
 "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}",
 "]",",","|",":",";","<",">",".","?","/"
]

def index(request):
    return render(request, 'index.html')

def generate(request):
    password = ''
    if request.method == "GET":
        if len(password) < 15:
            for i in range(15):
                password += random.choice(characters)
                print(password)
    return HttpResponse(password)            


