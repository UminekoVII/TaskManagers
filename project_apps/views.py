from django.shortcuts import render, redirect
from django.views import View
from .models import Users, Courses

# Create your views here.

class Sign_up(View):

    def get(self,request):
        return render(request, "../../final_project/templates/signup.html",{})

